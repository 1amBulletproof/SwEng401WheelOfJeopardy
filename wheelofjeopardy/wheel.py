"""
Wraps the sector classes and controls which sector affects the game_state
"""
from wheelofjeopardy.sectors import *
from wheelofjeopardy.category import Category

import random

#@TODO: create unit tests for this class
class Wheel(object):
    def __init__(self):
        self.description = 'Wheel from the game Wheel of Jeopardy!'
        self._sectors = self._initialize_sectors()

    #@TODO: update sectors for actual physical implementations available
    def _initialize_sectors(self):
        sector1 = bankrupt_sector.BankruptSector()
        sector2 = free_turn_sector.FreeTurnSector()
        sector3 = lose_turn_sector.LoseTurnSector()
        sector4 = spin_again_sector.SpinAgainSector()
        sector5 = opponent_choice_sector.OpponentChoiceSector()
        sector6 = player_choice_sector.PlayerChoiceSector()
        sector7 = board_sector.BoardSector(Category.category1)
        sector8 = board_sector.BoardSector(Category.category2)
        sector9 = board_sector.BoardSector(Category.category3)
        sector10 = board_sector.BoardSector(Category.category4)
        sector11 = board_sector.BoardSector(Category.category5)
        sector12 = board_sector.BoardSector(Category.category6)
        return [sector1, sector2, sector3, sector4,
                sector5, sector6, sector7, sector8,
                sector9, sector10, sector11, sector12]

    """
    get random sector, notify GUI of this sector (to show/animate it), and return the random sector
    """
    #@TODO:unfinished method
    def get_random_sector(self):
        random_number = random.randrange(0, len(self._sectors), 1)
        return self._sectors[random_number]


    def __str__(self):
        return self.description
