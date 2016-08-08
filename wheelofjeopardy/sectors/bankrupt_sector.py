"""
Logic for player landing on "bankrupt" sector of Wheel
"""
#@TODO unit tests
from wheelofjeopardy.sectors.sector import Sector

class BankruptSector(Sector):
    def __init__ (self):
        Sector.__init__(self, "bankrupt sector")

    def action(self, game_state):
        player = game_state.get_current_player()
        player.reset_score()
        game_state.end_turn()
