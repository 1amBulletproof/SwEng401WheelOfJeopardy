"""
Sector Super Class
"""

#@TODO: unit tests for class
class Sector:
    def __init__(self, name, events):
        self.name = name
        self.events = events

    def action(self, game_state):
        pass

    def __str__(self):
        return self.name
