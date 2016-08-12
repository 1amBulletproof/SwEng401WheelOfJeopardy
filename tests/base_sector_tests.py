import unittest

from tests.support import TestEvents

from wheelofjeopardy.sectors.sector import Sector
from wheelofjeopardy.game_state import GameState
from wheelofjeopardy.events import Events
from wheelofjeopardy.game_state import GameState
from wheelofjeopardy.player_state import PlayerState
from wheelofjeopardy.question_board_state import QuestionBoardState
from wheelofjeopardy.utils.read_configs import read_cfg_to_options
from wheelofjeopardy.category import Category

class TestSector(unittest.TestCase):
    def setUp(self):
        self.sector = Sector("base class")
        self.opts = read_cfg_to_options()
        self.events = TestEvents()
        self.player1 = PlayerState(name='Arthur', events=self.events)
        self.player2 = PlayerState(name='Lancelot', events=self.events)
        self.game_state = GameState([self.player1, self.player2], self.events, self.opts)
        self.category = Category()

        # check for game state setup events
        self.assertTrue(self.events.did_broadcast('game_state.spins_did_update'))
        self.assertTrue(self.events.did_broadcast('game_state.current_player_did_change'))

        # clear out setup events
        self.events.reset()

class TestBaseSector(TestSector):
    def test_name_attribute(self):
        self.assertEqual(self.sector.name, "base class")
        self.assertEqual(str(self.sector), "base class")

    def test_wager_amount(self):
        self.assertEqual(self.sector.MINIMUM_WAGER_AMOUNT, 5)

    def test_action(self):
        with self.assertRaises(NotImplementedError):
            self.sector.action(self.game_state)

#@TODO: test all the sector methods which do not return anything
#       but rather call events.broadcast()


if __name__ == '__main__':
    unittest.main()
