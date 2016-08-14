"""
Logic for player landing on any "normal" board sector of Wheel
"""
#@todo unit tests
from wheelofjeopardy.sectors.sector import Sector

class BoardSector(Sector):
    def __init__ (self, category):
        Sector.__init__(self, 'category %d' % category)
        self.category = category

    def action(self, game_state):
        game_state.current_category = self.category
        self.ask_next_question_in_category(self.category, game_state)
