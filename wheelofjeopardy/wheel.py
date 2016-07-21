"""
Wraps the sector classes and controls which affect the game_state
"""

from wheelofjeopardy.sectors import *

#@TODO: create unit tests for this class
class Wheel(object):
    #@TODO: initialization incomplete?
    def __init__(self):
        # self._sectors = self._initialize_sectors()

    #@TODO: update sectors for actual physical implementations available
    def _initialize_sectors(self):
        # sector1 = Section1()
        # sector2 =
        # sector3 =
        # sector4 =
        # sector5 =
        # sector6 =
        # .
        # .
        # .
        # sector12 =
        # return [sector1, sector2, sector3, sector4, sector5, sector6 ... sector12]

    """
    get random sector, notify GUI of this sector (to show/animate it), and pass game_state to the random sector's action() method
    """
    #@TODO:unfinished method
    def spin(self, game_state, gui):
        # self.current_sector = self._get_random_sector()
        # #Notify GUI? GUI Observers?
        # self.current_sector.action(game_state)

    #@TODO: get random number and return that index of self._sectors
    def _get_random_sector(self):
