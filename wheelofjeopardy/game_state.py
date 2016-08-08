"""
Control and monitor the wheelofjeopardy game state
"""

from wheelofjeopardy.question_board_state import QuestionBoardState
from wheelofjeopardy.wheel import Wheel

class GameState(object):
    def __init__(self, player_states, events, opts):
        self.events = events
        self.spins_remaining = opts.totalSpins
        self.player_states = player_states
        self.current_player_index = 0
        self.board = QuestionBoardState(events, opts)
        self.wheel = Wheel()
        self.active_wager = 0 # placeholder
        self.current_round = 1
        self.current_category = None # these three will be set by methods
        self.current_question = None
        self.current_sector = None

        self.events.subscribe('gui.category_chosen', self._on_category_chosen)
        self.events.subscribe('gui.answer_received', self._on_answer_received)
        self.events.subscribe('gui.correct_answer_received', self._on_correct_answer_received)
        self.events.subscribe('gui.incorrect_answer_received', self._on_incorrect_answer_received)

        # broadcast initial values
        self._broadcast('spins_did_update', self)
        self._broadcast('current_player_did_change', self)

    def get_current_player(self):
        return self.player_states[self.current_player_index]

    def any_spins_remaining(self):
        return self.spins_remaining > 0

    def spin(self):
        self.current_sector = self.wheel.get_random_sector()
        self.spins_remaining -= 1
        self._broadcast('sector_was_chosen', self.current_sector)
        self._broadcast('spins_did_update', self)
        self.current_sector.action(self)

        if self.has_game_ended():
            self._broadcast('game_did_end', self)

    def next_question_in_category(self, category):
        return self.board.next_q_in_category(self.current_round, category)

    def end_turn(self):
        self._broadcast('turn_will_end', self)
        if self.has_round_ended():
            if self.current_round == 1:
                self.current_round += 1
                self._broadcast('round_did_end')
            elif self.current_round == 2:
                self._broadcast('turn_did_end', self)
                self._broadcast('game_did_end', self)
                return
        self._choose_next_player()
        self._broadcast('turn_did_end', self)
        self._broadcast('current_player_did_change', self)

    def has_game_ended(self):
        return self.board.no_more_q()

    def has_round_ended(self):
        return self.board.no_q_in_round(self.current_round) or not self.any_spins_remaining()
    # private
    def _broadcast(self, channel, *args):
        self.events.broadcast('game_state.%s' % channel, *args)

    def _choose_next_player(self):
        self.current_player_index = \
            (self.current_player_index + 1) % len(self.player_states)

    def _on_category_chosen(self, category):
        self.current_sector.process_question(self)

    def _on_answer_received(self, answer):
        self.current_sector.receive_answer(self, self.current_question, answer)

    def _on_correct_answer_received(self, question):
        self.current_sector.received_correct_answer(self, question)

    def _on_incorrect_answer_received(self, question):
        self.current_sector.received_incorrect_answer(self, question)
