"""
Logic for player landing on "player choice" sector of Wheel
"""
#@todo unit tests
from wheelofjeopardy.sectors.sector import Sector

class PlayerChoiceSector(Sector):
    def __init__ (self):
        Sector.__init__(self, "player choice sector")

    def action(self, game_state):
        pass
