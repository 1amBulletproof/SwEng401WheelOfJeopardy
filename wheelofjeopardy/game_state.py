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
        self.wheel = Wheel(events)
        self.active_wager = 0 # placeholder
        self.current_round = 1
        self.current_category

        # broadcast initial values
        self._broadcast('spins_did_update', self)
        self._broadcast('current_player_did_change', self)

    def get_current_player(self):
        return self.player_states[self.current_player_index]

    def any_spins_remaining(self):
        return self.spins_remaining > 0

    def spin(self):
        self.current_sector = self.wheel.get_random_sector()
        # are these both needed? only included 1 in sequence diagram
        self._broadcast('sector_will_apply', self, self.current_sector)
        self._broadcast('sector_did_apply', self, self.current_sector)
        self.current_sector.action(self)
        self.spins_remaining -= 1
        self._broadcast('spins_did_update', self)

        if self.has_game_ended():
            self._broadcast('game_did_end', self)

    def set_category(self, category):
        self.current_category = category
        _process_a_question()

    def _process_a_question(self):
        events = game_state.events
        board_state = game_state.board
        round = game_state.current_round
        if board_state.no_q_in_round(round):
            if (round == 1):
                game_state.current_round += 1
                round += 1
                events.broadcast('game_state.round_did_end')
            elif (round == 2):
                events.broadcast('game_state.game_did_end')
        elif board_state.no_q_in_category(round, category):
            events.broadcast('game_state.prompt_no_remaining_question_spin_again')
            break
        else:
            question = board_state.next_q_in_category(round, category)
            events.broadcast('game_state.question_will_be_asked', question)

    def end_turn(self):
        self._broadcast('turn_will_end', self)
        self._choose_next_player()
        self._broadcast('turn_did_end', self)
        self._broadcast('current_player_did_change', self)

    def has_game_ended(self):
        return self.board.no_more_q()

    # private
    def _broadcast(self, channel, *args):
        self.events.broadcast('game_state.%s' % channel, *args)

    def _choose_next_player(self):
        self.current_player_index = \
            (self.current_player_index + 1) % len(self.player_states)
