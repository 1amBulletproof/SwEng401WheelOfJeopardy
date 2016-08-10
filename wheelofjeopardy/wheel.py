"""
Wraps the sector classes and controls which sector affects the game_state
"""
from wheelofjeopardy.sectors import *
from wheelofjeopardy.category import Category
import random

import random

#@TODO: create unit tests for this class
class Wheel(object):
    def __init__(self):
        self.description = 'Wheel from the game Wheel of Jeopardy!'
        self._sectors = self._initialize_sectors()

    def _initialize_sectors(self):
        sector1 = board_sector.BoardSector(Category.category1)
        sector2 = board_sector.BoardSector(Category.category2)
        sector3 = board_sector.BoardSector(Category.category3)
        sector4 = board_sector.BoardSector(Category.category4)
        sector5 = board_sector.BoardSector(Category.category5)
        sector6 = board_sector.BoardSector(Category.category6)
        sector7 = bankrupt_sector.BankruptSector()
        sector8 = free_turn_sector.FreeTurnSector()
        sector9 = lose_turn_sector.LoseTurnSector()
        sector10 = spin_again_sector.SpinAgainSector()
        sector11 = opponent_choice_sector.OpponentChoiceSector()
        sector12 = player_choice_sector.PlayerChoiceSector()

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

    def _get_sector(self, ind):
        if ind >= len(self._sectors):
            raise IndexError('Invalid sector choice.')
        return self._sectors[ind]

    def __str__(self):
        return self.description
