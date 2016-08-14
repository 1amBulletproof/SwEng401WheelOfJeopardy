"""
Control and monitor the wheelofjeopardy game state
"""

from wheelofjeopardy.question_timer import QuestionTimer
from wheelofjeopardy.question_board_state import QuestionBoardState
from wheelofjeopardy.wheel import Wheel
from wheelofjeopardy.fake_wheel import FakeWheel

class GameState(object):
    def __init__(self, player_states, events, opts):
        self.events = events
        self.TOTAL_SPINS = opts.total_spins
        self.spins_remaining = self.TOTAL_SPINS
        self.player_states = player_states
        self.current_player_index = 0
        self.board = QuestionBoardState(events, opts)

        if len(opts.programmed_spins) == 0: # no programmed spins
            self.wheel = Wheel()
        else: # wheel programmed to spin according to list
            self.wheel = FakeWheel(opts.programmed_spins)

        self.active_wager = None # placeholder
        self.current_round = 1
        self.current_category = None # these three will be set by methods
        self.current_question = None
        self.current_sector = None

        self.events.subscribe('gui.game_will_start', self._on_game_will_start)
        self.events.subscribe('gui.spin', self._on_spin)
        self.events.subscribe('gui.category_chosen', self._on_category_chosen)
        self.events.subscribe('gui.answer_received', self._on_answer_received)
        self.events.subscribe('gui.correct_answer_received', self._on_correct_answer_received)
        self.events.subscribe('gui.incorrect_answer_received', self._on_incorrect_answer_received)

        self.events.subscribe('gui.use_free_token', self._on_use_free_token)
        self.events.subscribe('gui.dont_use_free_token', self._on_dont_use_free_token)
        self.events.subscribe('gui.wager_received', self._on_wager_received)

        self.events.subscribe('question_timer.has_expired', self._question_timer_has_expired)

        self.timer = QuestionTimer(
            events=self.events, game_state=self, opts=opts
        )

    def get_current_player(self):
        return self.player_states[self.current_player_index]

    def any_spins_remaining(self):
        return self.spins_remaining > 0

    def spin(self, sect=None):
        self.current_question = None

        if sect is None:
            self.current_sector = self.wheel.get_random_sector()
        else:
            self.current_sector = self.wheel._get_sector(sect)

        print(self.current_sector)

        self.spins_remaining -= 1
        self._broadcast('sector_was_chosen', self.current_sector)
        self._broadcast('spins_did_update', self)
        self.current_sector.action(self)

        self.check_for_game_or_round_end()

    def check_for_game_or_round_end(self):
        if self.has_game_ended() or self.has_round_ended():
            self.end_turn()

    def start_timer(self):
        self.timer.start()

    def stop_timer(self):
        self.timer.stop()

    def _cheat(self, sect):
        if not sect.isdigit():
            raise ValueError('Second char is not a digit')
        else:
            self.spin(int(sect) - 1) # sector number needs to be subtracted

    def next_question_in_category(self, category):
        return self.board.next_q_in_category(self.current_round, category)

    def end_turn(self):
        self._broadcast('turn_will_end', self)

        if self.has_round_ended():
            if self.has_game_ended():
                self._broadcast('turn_did_end', self)
                self._broadcast('game_did_end', self)
                self._broadcast('announce_winners', self._calculate_winner())
                return
            else:
                self._broadcast('round_did_end', self)
                self.advance_round()

        self._choose_next_player()
        self._broadcast('turn_did_end', self)
        self._broadcast('current_player_did_change', self)

    def has_game_ended(self):
        return self.has_round_ended() and self.current_round == 2 \
            and self.current_question == None

    def has_round_ended(self):
        return (self.board.no_q_in_round(self.current_round) or \
            not self.any_spins_remaining()) and \
            self.current_question == None

    def advance_round(self):
        self.spins_remaining = self.TOTAL_SPINS # reset spin count
        self._broadcast('spins_did_update', self)
        self.board.mark_all_q_used(self.current_round) # use all questions
        self.current_round += 1
        # Does player sequence reset at round end? Or continue as it was?

    # private

    def _broadcast(self, channel, *args):
        self.events.broadcast('game_state.%s' % channel, *args)

    def _on_game_will_start(self):
        # broadcast initial values
        self._broadcast('spins_did_update', self)
        self._broadcast('current_player_did_change', self)

    def _on_spin(self):
        self.spin()

    def _choose_next_player(self):
        self.current_player_index = \
            (self.current_player_index + 1) % len(self.player_states)

    def _on_category_chosen(self, category):
        self.current_category = category
        self.current_sector.process_question(self)

    def _on_answer_received(self, answer):
        self.stop_timer()
        self.current_sector.receive_answer(self, self.current_question, answer)

    def _on_correct_answer_received(self, question):
        self.current_sector.received_correct_answer(self, question)

    def _on_incorrect_answer_received(self, question):
        self.current_sector.received_incorrect_answer(self, question)

    def _question_timer_has_expired(self):
        # treat an expired timer the same as an incorrect answer
        self.current_sector.received_incorrect_answer(self, self.current_question)

    def _on_use_free_token(self):
        self.current_sector.received_use_free_token(self)

    def _on_dont_use_free_token(self):
        self.current_sector.received_dont_use_free_token(self)

    def _on_wager_received(self, amount):
        self.current_sector.received_wager_amount(self, amount)

    def _calculate_winner(self):
        '''
        Return a list of strings where the strings are the names of winners
        '''
        scores = [pl.score for pl in self.player_states] # all scores in list
        winning_score = max(scores) # high score, the winner
        winners = [pl.name for pl in self.player_states \
                   if pl.score == winning_score]

        return winners
