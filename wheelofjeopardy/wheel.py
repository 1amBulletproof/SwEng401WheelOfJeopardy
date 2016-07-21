"""
Wraps the sector classes and controls which affect the game_state
"""

from wheelofjeopardy.sectors.sector import Sector

# placeholder
class Wheel(object):
    def __init__(self, events):
      self.events = events

    def spin(self):
        return Sector()  # return generic sector for now
