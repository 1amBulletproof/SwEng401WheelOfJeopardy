"""
Sector Super Class
"""

<<<<<<< HEAD
#@TODO: unit tests for class
class Sector:
    def __init__(self, name):
        self.name = name

    def action(self):
        raise NotImplementedError()
=======
# placeholder
class Sector(object):
    def apply_to(self, game_state):
        game_state.end_turn()
        pass
>>>>>>> dc79324844d2c190216741995b1bfe24f37c9209
