"""
Logic for player landing on "lose turn" sector of Wheel
"""
#@todo unit tests
from wheelofjeopardy.sectors.sector import Sector

class LoseTurnSector(Sector):
    def __init__ (self):
        Sector.__init__(self, "lose turn sector")

    def action(self, game_state):
        if game_state.get_current_player().has_free_spin_token():
            game_state.events.broadcast('sector.prompt_for_token_use')
        else:
            game_state.end_turn()
