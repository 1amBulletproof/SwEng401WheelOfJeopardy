"""
Logic for player landing on "free turn" sector of Wheel
"""
#@todo unit tests
from wheelofjeopardy.sectors.sector import Sector

class FreeTurnSector(Sector):
    def __init__ (self):
        Sector.__init__(self, "free turn sector")

    def action(self, game_state):
        pass
