"""
Logic for player landing on "player choice" sector of Wheel
"""
#@todo unit tests
from wheelofjeopardy.sectors.sector import Sector

class PlayerChoiceSector(Sector):
    def __init__ (self):
        Sector.__init__(self, "player choice sector")

    def action(self, game_state):
        #gui is listening
        game_state.events.broadcast('player_choice_sector.choose_category',
                                    'Player')

    def process_question(self, game_state):
        Sector.ask_next_question_in_category(self, game_state.current_category, game_state)
