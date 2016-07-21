import unittest

from tests.support import TestEvents
from wheelofjeopardy.player_state import PlayerState, NoTokensAvailableError

class PlayerStateTestCase(unittest.TestCase):
    def setUp(self):
        self.events = TestEvents()
        self.player_state = PlayerState(name='Monty', events=self.events)

class TestInitialPlayerState(PlayerStateTestCase):
    def test_name_attribute(self):
        self.assertEqual(self.player_state.name, 'Monty')

    def test_zero_score(self):
        self.assertEqual(self.player_state.score, 0)

    def test_zero_free_spin_tokens(self):
        self.assertEqual(self.player_state.free_spin_tokens, 0)

class TestScoreControls(PlayerStateTestCase):
    def test_increases_score(self):
        self.assertEqual(self.player_state.score, 0)
        self.player_state.increase_score_by(10)
        self.assertEqual(self.player_state.score, 10)

    def test_score_increase_fires_event(self):
        self.player_state.increase_score_by(10)
        self.assertTrue(self.events.did_broadcast('player_state.score_did_update'))

    def test_decreases_score(self):
        self.assertEqual(self.player_state.score, 0)
        self.player_state.decrease_score_by(10)
        self.assertEqual(self.player_state.score, -10)

    def test_score_decrease_fires_event(self):
        self.player_state.decrease_score_by(10)
        self.assertTrue(self.events.did_broadcast('player_state.score_did_update'))

class TestFreeSpinTokenControls(PlayerStateTestCase):
    def test_increases_tokens(self):
        self.assertEqual(self.player_state.free_spin_tokens, 0)
        self.player_state.grant_free_spin_token()
        self.assertEqual(self.player_state.free_spin_tokens, 1)

    def test_token_increase_fires_event(self):
        self.player_state.grant_free_spin_token()
        self.assertTrue(self.events.did_broadcast('player_state.spin_tokens_did_update'))

    def test_decreases_tokens(self):
        self.player_state.grant_free_spin_token()
        self.assertEqual(self.player_state.free_spin_tokens, 1)
        self.player_state.use_free_spin_token()
        self.assertEqual(self.player_state.free_spin_tokens, 0)

    def test_token_decrease_fires_event(self):
        self.player_state.free_spin_tokens = 1
        self.player_state.use_free_spin_token()
        self.assertTrue(self.events.did_broadcast('player_state.spin_tokens_did_update'))

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
