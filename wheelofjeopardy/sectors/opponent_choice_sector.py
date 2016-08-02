"""
Logic for player landing on "opponent choice" sector of Wheel
"""
#@todo unit tests
from wheelofjeopardy.sectors.sector import Sector

class OpponentChoiceSector(Sector):
    def __init__ (self):
        Sector.__init__(self, "opponent choice sector")

    def action(self, game_state):
        events.broadcast('opponent_choice_sector.choose_cateogry')
