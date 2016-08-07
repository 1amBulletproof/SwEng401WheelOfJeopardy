"""
Sector Super Class

action() method MUST be overriden by sub-classes
"""

#@TODO: unit tests for class
class Sector:
    def __init__(self, name):
        self.name = name
        self.events = events

    def action(self, game_state):
        raise NotImplementedError

    def __str__(self):
        return self.name
