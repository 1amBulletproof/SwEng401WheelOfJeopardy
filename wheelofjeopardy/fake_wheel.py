"""
Wraps the sector classes and controls which sector affects the game_state
"""
from wheelofjeopardy.sectors import *
from wheelofjeopardy.category import Category
import random

#@TODO: create unit tests for this class
class FakeWheel(object):
    def __init__(self, steps=None):
        self.description = 'Wheel from the game Wheel of Jeopardy!'
        self._sectors = self._initialize_sectors()

        if steps == None:
            #function for loading steps from a file here
            # self.steps = _load_steps()
        else:
            self.steps = steps
        self.count = -1 # initialized to unused

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
        # random_number = random.randrange(0, len(self._sectors), 1)
        return self._sectors[ self._next_pretermined() ]

    def _get_sector(self, ind):
        if ind >= len(self._sectors) or ind < 0:
            raise IndexError('Invalid sector choice.')
        return self._sectors[ind]

    def _next_predetermined(self):
        self.count += 1
        if self.count > len(self.steps): # loops back to first if exhaust steps
            self.count = 0
        return self.steps[self.count]

    def __str__(self):
        return self.description
