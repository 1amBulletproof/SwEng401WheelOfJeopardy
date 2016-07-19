import unittest

from wheelofjeopardy.game_state import GameState
from wheelofjeopardy.player_state import PlayerState
from wheelofjeopardy.question_board_state import QuestionBoardState
from wheelofjeopardy.wheel import Wheel

class GameStateTestCase(unittest.TestCase):
    def setUp(self):
      self.player1 = PlayerState(name='Arthur')
      self.player2 = PlayerState(name='Lancelot')
      self.game_state = GameState([self.player1, self.player2])

class TestInitialGameState(GameStateTestCase):
    def test_number_of_remaining_spins(self):
      self.assertEqual(self.game_state.spins_remaining, 50)

    def test_player_states(self):
      self.assertEqual(
        self.game_state.player_states, [self.player1, self.player2]
      )

    def test_board_type(self):
      self.assertEqual(type(self.game_state.board), QuestionBoardState)

    def test_wheel_type(self):
      self.assertEqual(type(self.game_state.wheel), Wheel)

    def test_current_player_is_first_player(self):
      current_player = self.game_state.get_current_player()
      self.assertEqual(current_player.name, self.player1.name)

    def test_any_spins_remaining(self):
      self.assertTrue(self.game_state.any_spins_remaining)

    def test_spin_decrements_spins_remaining(self):
      self.assertEqual(self.game_state.spins_remaining, 50)
      self.game_state.spin()
      self.assertEqual(self.game_state.spins_remaining, 49)

class TestEndTurn(GameStateTestCase):
    def test_end_of_turn_chooses_next_player(self):
      self.assertEqual(self.game_state.get_current_player().name, 'Arthur')
      self.game_state.end_turn()
      self.assertEqual(self.game_state.get_current_player().name, 'Lancelot')

    def test_end_of_turn_alternates_players(self):
      self.assertEqual(self.game_state.get_current_player().name, 'Arthur')
      self.game_state.end_turn()
      self.assertEqual(self.game_state.get_current_player().name, 'Lancelot')
      self.game_state.end_turn()
      self.assertEqual(self.game_state.get_current_player().name, 'Arthur')

class TestEndGame(GameStateTestCase):
    def test_game_end_when_no_more_questions(self):
      self.assertFalse(self.game_state.has_game_ended())
      self.game_state.board.questions_remaining = 0
      self.assertTrue(self.game_state.has_game_ended())

    def test_game_end_when_no_more_spins(self):
      self.assertFalse(self.game_state.has_game_ended())
      self.game_state.spins_remaining = 0
      self.assertTrue(self.game_state.has_game_ended())
