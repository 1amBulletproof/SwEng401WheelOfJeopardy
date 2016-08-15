"""
Logic for player landing on "opponent choice" sector of Wheel
"""
#@todo unit tests
from wheelofjeopardy.sectors.sector import Sector

class OpponentChoiceSector(Sector):
    def __init__ (self):
        Sector.__init__(self, "opponent's choice")

    def action(self, game_state):
        game_state.events.broadcast('opponent_choice_sector.choose_category')

    def process_question(self, game_state):
        self.ask_next_question_in_category(game_state.current_category, game_state)
