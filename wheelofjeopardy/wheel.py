"""
Wraps the sector classes and controls which affect the game_state
"""
#FARHEEN COMMENT
import random
from wheelofjeopardy.sectors.sector import *

#@TODO: create unit tests for this class
class Wheel(object):
    #@TODO: initialization incomplete?
    def __init__(self, event):
        self.description = 'Wheel from the game Wheel of Jeopardy!'
        pass
        # self._sectors = self._initialize_sectors()

    #@TODO: update sectors for actual physical implementations available
    def _initialize_sectors(self):
        pass
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
    get random sector, notify GUI of this sector (to show/animate it), and return the random sector
    """
    #@TODO:unfinished method
    def get_random_sector(self):
        self.sector_selected = Sector("random sector")
        return self.sector_selected
        # self.current_sector = self._get_random_sector()
        # #Notify GUI? GUI Observers?
        # self.current_sector.action(game_state) - handled by the game_state currently
        # return self.current_sector

    #@TODO: get random number and return that index of self._sectors
    def _get_random_sector(self):
        return random.randrange(len(self._sectors))
        pass


    def __str__(self):
        return self.description
