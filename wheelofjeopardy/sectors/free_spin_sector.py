"""
Logic for player landing on "free turn" sector of Wheel
"""
#@todo unit tests
from wheelofjeopardy.sectors.sector import Sector

class FreeSpinSector(Sector):
    def __init__ (self):
        Sector.__init__(self, 'free spin sector')

    def action(self, game_state):
        player = game_state.get_current_player()
        player.grant_free_spin_token()
