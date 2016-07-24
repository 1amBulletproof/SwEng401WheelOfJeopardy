"""
Control and monitor the wheelofjeopardy game state
"""

from wheelofjeopardy.question_board_state import QuestionBoardState
from wheelofjeopardy.wheel import Wheel

class GameState(object):
    TOTAL_SPINS = 50

    def __init__(self, player_states, events):
        self.events = events
        self.spins_remaining = GameState.TOTAL_SPINS
        self.player_states = player_states
        self.current_player_index = 0
        self.board = QuestionBoardState(events)
        self.wheel = Wheel(events)

        # broadcast initial values
        self._broadcast('spins_did_update', self)
        self._broadcast('current_player_did_change', self)

    def get_current_player(self):
        return self.player_states[self.current_player_index]

    def any_spins_remaining(self):
        return self.spins_remaining > 0

    def spin(self):
        sector = self.wheel.spin()
        self._broadcast('sector_will_apply', self, sector) # are these both needed? only included 1 in sequence diagram
        self._broadcast('sector_did_apply', self, sector) # are these both needed? only included 1 in sequence diagram
        sector.action(self)
        self.spins_remaining -= 1
        self._broadcast('spins_did_update', self)

        if self.has_game_ended():
            self._broadcast('game_did_end', self)

    def end_turn(self):
        self._broadcast('turn_will_end', self)
        self._choose_next_player()
        self._broadcast('turn_did_end', self)
        self._broadcast('current_player_did_change', self)

    def has_game_ended(self):
        return (not self.board.any_questions_remaining()) or (not self.any_spins_remaining())

    # private

    def _broadcast(self, channel, *args):
        self.events.broadcast('game_state.%s' % channel, *args)

    def _choose_next_player(self):
        self.current_player_index = (self.current_player_index + 1) % len(self.player_states)
