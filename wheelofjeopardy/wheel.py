"""
Wraps the sector classes and controls which sector affects the game_state
"""

from wheelofjeopardy.sectors.sector import *

#@TODO: create unit tests for this class
class Wheel(object):
    def __init__(self, event):
        self.description = 'Wheel from the game Wheel of Jeopardy!'
        self._sectors = self._initialize_sectors()

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
    get random sector, notify GUI of this sector (to show/animate it)
    and return the random sector
    """
    def get_random_sector(self):
        random_number = random.randrange(0, 11, 1)
        return self._sectors[random_number]

    def __str__(self):
        return self.description
