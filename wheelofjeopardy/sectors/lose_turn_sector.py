"""
Logic for player landing on "lose turn" sector of Wheel
"""

from wheelofjeopardy.sectors.sector import Sector

class LoseTurnSector(Sector):
    def __init__ (self):
        Sector.__init__(self, "lose turn")

    def action(self, game_state):
        game_state.end_turn()
