"""
Logic for player landing on "lose turn" sector of Wheel
"""
#@todo unit tests
from wheelofjeopardy.sectors.sector import Sector

class LoseTurnSector(Sector):
    def __init__ (self):
        Sector.__init__(self, "lose turn sector")

    def action(self, game_state):
        game_state.end_turn()
