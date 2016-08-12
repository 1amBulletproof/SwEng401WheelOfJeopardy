"""
The FakeWheel returns pre-determined spins passed into constructor.

Inherits the Wheel class
"""
#from wheelofjeopardy.sectors import *
#from wheelofjeopardy.category import Category
from wheelofjeopardy.wheel import Wheel

class FakeWheel(Wheel):
    def __init__(self, steps):
        super(FakeWheel, self).__init__() # use Wheel class constructor

        self.steps = [x-1 for x in steps] # sectors are 0-indexed
        self.count = -1 # initialized to unused

    '''
    Get a "random" sector based on pre-determined as in self.steps
    '''
    def get_random_sector(self):
        return self._sectors[ self._next_predetermined() ]

    def _next_predetermined(self):
        # loops back to first step if no more steps
        self.count = (self.count+1) % len(self.steps)
        return self.steps[self.count]

