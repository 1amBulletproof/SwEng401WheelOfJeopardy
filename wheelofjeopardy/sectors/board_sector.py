"""
Logic for player landing on any "normal" board sector of Wheel
"""
#@todo unit tests
from wheelofjeopardy.sectors.sector import Sector

class BoardSector(Sector):
    def __init__ (self, category):
        Sector.__init__(self, "Board sector " + str(category))
        self.category = category

    #@TODO Apply Question Selection logic (i.e. are there any questions left: see sequence diagram)
    def action(self, game_state):
        game_state.set_category(self.category)
