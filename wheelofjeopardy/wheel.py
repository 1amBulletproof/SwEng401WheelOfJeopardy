"""
Wraps the sector classes and controls which sector affects the game_state
"""

from wheelofjeopardy.sectors import *
from wheelofjeopardy.category import Category

#@TODO: create unit tests for this class
class Wheel(object):
    def __init__(self):
        self.description = 'Wheel from the game Wheel of Jeopardy!'
        self._sectors = self._initialize_sectors()

    #@TODO: update sectors for actual physical implementations available
    def _initialize_sectors(self):
        sector1 = BankruptSector()
        sector2 = FreeTurnSector()
        sector3 = LoseTurnSector()
        sector4 = SpinAgainSector()
        sector5 = OpponentChoiceSector()
        sector6 = PlayerChoiceSector()
        sector7 = BoardSector(Category.category1)
        sector8 = BoardSector(Category.category2)
        sector9 = BoardSector(Category.category3)
        sector10 = BoardSector(Category.category4)
        sector11 = BoardSector(Category.category5)
        sector12 = BoardSector(Category.category6)
        return [sector1, sector2, sector3, sector4 \
                ,sector5, sector6, sector7, sector8 \
                ,sector9, sector10, sector11, sector12]

    def get_random_sector(self):
        random_number = random.randrange(0, 11, 1)
        return self._sectors[random_number]

    def __str__(self):
        return self.description
