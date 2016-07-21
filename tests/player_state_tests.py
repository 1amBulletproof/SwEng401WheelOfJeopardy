import unittest

from wheelofjeopardy.events import Events
from wheelofjeopardy.player_state import PlayerState, NoTokensAvailableError

class PlayerStateTestCase(unittest.TestCase):
    def setUp(self):
        events = Events()
        self.player_state = PlayerState(name='Monty', events=events)

class TestInitialPlayerState(PlayerStateTestCase):
    def test_name_attribute(self):
        self.assertEqual(self.player_state.name, 'Monty')

    def test_zero_score(self):
        self.assertEqual(self.player_state.score, 0)

    def test_zero_free_spin_tokens(self):
        self.assertEqual(self.player_state.free_spin_tokens, 0)

class TestScoreControls(PlayerStateTestCase):
    def setUp(self):
        events = Events()
        self.player_state = PlayerState(name='Monty', events=events)

    def test_increases_score(self):
        self.assertEqual(self.player_state.score, 0)
        self.player_state.increase_score_by(10)
        self.assertEqual(self.player_state.score, 10)

    def test_decreases_score(self):
        self.assertEqual(self.player_state.score, 0)
        self.player_state.decrease_score_by(10)
        self.assertEqual(self.player_state.score, -10)

class TestFreeSpinTokenControls(PlayerStateTestCase):
    def test_increases_tokens(self):
        self.assertEqual(self.player_state.free_spin_tokens, 0)
        self.player_state.grant_free_spin_token()
        self.assertEqual(self.player_state.free_spin_tokens, 1)

    def test_decreases_tokens(self):
        self.player_state.grant_free_spin_token()
        self.assertEqual(self.player_state.free_spin_tokens, 1)
        self.player_state.use_free_spin_token()
        self.assertEqual(self.player_state.free_spin_tokens, 0)

    def test_raises_error_when_no_tokens_available(self):
        self.assertEqual(self.player_state.free_spin_tokens, 0)

        with self.assertRaises(NoTokensAvailableError):
            self.player_state.use_free_spin_token()

    def test_reports_available_tokens(self):
        self.player_state.grant_free_spin_token()
        self.assertEqual(self.player_state.free_spin_tokens, 1)
        self.assertTrue(self.player_state.has_free_spin_token())

    def test_reports_no_available_tokens(self):
        self.assertEqual(self.player_state.free_spin_tokens, 0)
        self.assertFalse(self.player_state.has_free_spin_token())

if __name__ == '__main__':
    unittest.main()
