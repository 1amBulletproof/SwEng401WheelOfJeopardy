"""
Logic for player landing on "spin again" sector of Wheel
"""
#@todo unit tests
from wheelofjeopardy.sectors.sector import Sector

class SpinAgainSector(Sector):
    def __init__ (self):
        Sector.__init__(self, 'spin again')

    """
    as currently implemented, should do nothing since game_state will
    decrement the spins and broadcast that event (deviates slightly from sequence diagram)
    """
    def action(self, game_state):
        pass
