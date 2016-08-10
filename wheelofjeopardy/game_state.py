"""
Control and monitor the wheelofjeopardy game state
"""

from wheelofjeopardy.question_board_state import QuestionBoardState
from wheelofjeopardy.wheel import Wheel

class GameState(object):
    def __init__(self, player_states, events, opts):
        self.events = events
        self.TOTAL_SPINS = opts.totalSpins
        self.spins_remaining = self.TOTAL_SPINS
        self.player_states = player_states
        self.current_player_index = 0
        self.board = QuestionBoardState(events, opts)
        self.wheel = Wheel()
        self.active_wager = None # placeholder
        self.current_round = 1
        self.current_category = None # these three will be set by methods
        self.current_question = None
        self.current_sector = None

        self.events.subscribe('gui.category_chosen', self._on_category_chosen)
        self.events.subscribe('gui.answer_received', self._on_answer_received)
        self.events.subscribe('gui.correct_answer_received', self._on_correct_answer_received)
        self.events.subscribe('gui.incorrect_answer_received', self._on_incorrect_answer_received)

        self.events.subscribe('gui.use_free_token', self._on_use_free_token)
        self.events.subscribe('gui.dont_use_free_token', self._on_dont_use_free_token)
        self.events.subscribe('gui.wager_received', self._on_wager_received)
        self.events.subscribe('gui.round_did_end', self.advance_round)
        self.events.subscribe('gui.game_did_end', self.game_has_ended)

        # broadcast initial values
        self._broadcast('spins_did_update', self)
        self._broadcast('current_player_did_change', self)

    def get_current_player(self):
        return self.player_states[self.current_player_index]

    def any_spins_remaining(self):
        return self.spins_remaining > 0

    def spin(self, sect=None):
        if sect is None:
            self.current_sector = self.wheel.get_random_sector()
        else:
            self.current_sector = self.wheel._get_sector(sect)
        self.spins_remaining -= 1
        self._broadcast('sector_was_chosen', self.current_sector)
        self._broadcast('spins_did_update', self)
        self.current_sector.action(self)

        if self.has_game_ended():
            game_has_ended()

    def game_has_ended(self):
            winner = self.calculate_winner()
            self._broadcast('announce_winner', self, winner)

    def _cheat(self, sect):
        if not sect.isdigit():
            raise ValueError('Second char is not a digit')
        else:
            self.spin( int(sect)-1 ) # sector number needs to be subtracted

    def next_question_in_category(self, category):
        return self.board.next_q_in_category(self.current_round, category)

    def end_turn(self):
        self._broadcast('turn_will_end', self)
        if self.has_round_ended():
            if not self.has_game_ended:
                # not sure if broadcasting is needed here
                # self._broadcast('round_did_end')
                self.advance_round()
            else:
                self._broadcast('turn_did_end', self)
                self._broadcast('game_did_end', self)
                return
        self._choose_next_player()
        self._broadcast('turn_did_end', self)
        self._broadcast('current_player_did_change', self)

    def has_game_ended(self):
        return self.board.no_more_q()

    def has_round_ended(self):
        return self.board.no_q_in_round(self.current_round) or \
            not self.any_spins_remaining()

    def advance_round(self):
        print('That concludes round %u.' % self.current_round )
        self.spins_remaining = self.TOTAL_SPINS # reset spin count
        self.board.mark_all_q_used(self.current_round) # use all questions
        self.current_round += 1
        # Does player sequence reset at round end? Or continue as it was?
    # private
    def _broadcast(self, channel, *args):
        self.events.broadcast('game_state.%s' % channel, *args)

    def _choose_next_player(self):
        self.current_player_index = \
            (self.current_player_index + 1) % len(self.player_states)

    def _on_category_chosen(self, category):
        self.current_category = category
        self.current_sector.process_question(self)

    def _on_answer_received(self, answer):
        self.current_sector.receive_answer(self, self.current_question, answer)

    def _on_correct_answer_received(self, question):
        self.current_sector.received_correct_answer(self, question)

    def _on_incorrect_answer_received(self, question):
        self.current_sector.received_incorrect_answer(self, question)

    def _on_use_free_token(self):
        self.current_sector.received_use_free_token(self)

    def _on_dont_use_free_token(self):
        self.current_sector.received_dont_use_free_token(self)

    def _on_wager_received(self, amount):
        self.current_sector.received_wager_amount(self, amount)

    def calculate_winner(self):
        winner = []
        #scores is a dictionary object, which means each element
        #has a key and a value
        #used this so the player name would be linked to the score
        scores = {}
        num_winners = 0
        num_players = len(self.player_states)
        for x in range(0, num_players-1):
            scores[self.player_states[x].name] = self.player_states[x].score
        #sort the scores
        sorted(scores.values(), key=int)
        #check for multiple winners
        #if there's more than one player
        if num_players > 1:
            #if the last and 2nd to last scores are equal
            #should this care if all scores are 0?
            for n in range(num_players-1, 1, -1):
                #THIS CAUSES AN ERROR
                #instead of -n for a number index, it is expecting
                #a string index since I defined this as a "dictionary"
                #list. Not sure how to make this logic work..
                if (scores[-n] == scores[-n-1]):
                    if n == 1:
                        num_winners = 2
                    #if any other scores are equal too
                    else:
                        num_winners += 1
        #finally add the player names to the list of winners
        for x in range(0, num_winners-1):
            for name, score in scores.iteritems():
                if score == scores[num_players-x]:
                    winner[x] = name
        winner_ret = ", ".join(winner)
        return winner_ret
        
