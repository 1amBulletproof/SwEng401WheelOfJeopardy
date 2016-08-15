import unittest

from tests.support import TestEvents

from wheelofjeopardy.sectors import *
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
        self.opts = read_cfg_to_options()
        self.events = TestEvents()
        self.player1 = PlayerState(name='Arthur', events=self.events)
        self.player2 = PlayerState(name='Lancelot', events=self.events)
        self.game_state = GameState([self.player1, self.player2], self.events, self.opts)
        self.category = Category()

        # check for game state setup events
        # self.assertTrue(self.events.did_broadcast('game_state.spins_did_update'))
        # self.assertTrue(self.events.did_broadcast('game_state.current_player_did_change'))

        # clear out setup events
        self.events.reset()

class TestBankruptSector(TestSector):
    def test_name(self):
        self.sector = bankrupt_sector.BankruptSector()
        self.assertEqual(self.sector.name, "bankrupt")
        self.assertEqual(str(self.sector), "bankrupt")

    def test_action(self):
        self.sector = bankrupt_sector.BankruptSector()
        self.player1.increase_score_by(10)
        self.assertTrue(self.player1.score == 10)
        self.sector.action(self.game_state)
        self.assertTrue(self.player1.score == 0)

class TestFreeSpin(TestSector):
    def test_name(self):
        self.sector = free_spin_sector.FreeSpinSector()
        self.assertEqual(self.sector.name, "free spin")
        self.assertEqual(str(self.sector), "free spin")

    def test_action(self):
        self.sector = free_spin_sector.FreeSpinSector()
        self.assertTrue(self.player1.free_spin_tokens == 0)
        self.sector.action(self.game_state)
        self.assertTrue(self.player1.free_spin_tokens == 1)

class TestLoseTurnSector(TestSector):
    def test_name(self):
        self.sector = lose_turn_sector.LoseTurnSector()
        self.assertEqual(self.sector.name, "lose turn")
        self.assertEqual(str(self.sector), "lose turn")

    # def test_action(self):

class TestSpinAgainSector(TestSector):
    def test_name(self):
        self.sector = spin_again_sector.SpinAgainSector()
        self.assertEqual(self.sector.name, "spin again")
        self.assertEqual(str(self.sector), "spin again")

    # def test_action(self):


class TestOpponentChoiceSector(TestSector):
    def test_name(self):
        self.sector = opponent_choice_sector.OpponentChoiceSector()
        self.assertEqual(self.sector.name, "opponent's choice")
        self.assertEqual(str(self.sector), "opponent's choice")

    # def test_action(self):


class TestPlayerChoiceSector(TestSector):
    def test_name(self):
        self.sector = player_choice_sector.PlayerChoiceSector()
        self.assertEqual(self.sector.name, "player's choice")
        self.assertEqual(str(self.sector), "player's choice")

    # def test_action(self):



if __name__ == "__main__":
  Unittest.main()
