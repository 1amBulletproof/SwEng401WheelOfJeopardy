import unittest

from tests.support import TestEvents

from wheelofjeopardy.events import Events
from wheelofjeopardy.game_state import GameState
from wheelofjeopardy.player_state import PlayerState
from wheelofjeopardy.question_board_state import QuestionBoardState
from wheelofjeopardy.utils.read_configs import ReadCfgToOptions
from wheelofjeopardy.wheel import Wheel

class GameStateTestCase(unittest.TestCase):
    def setUp(self):
        self.opts = ReadCfgToOptions()
        self.events = TestEvents()
        self.player1 = PlayerState(name='Arthur', events=self.events)
        self.player2 = PlayerState(name='Lancelot', events=self.events)
        self.game_state = GameState([self.player1, self.player2], self.events, self.opts)

        # check for game state setup events
        self.assertTrue(self.events.did_broadcast('game_state.spins_did_update'))
        self.assertTrue(self.events.did_broadcast('game_state.current_player_did_change'))

        # clear out setup events
        self.events.reset()

    def use_all_questions(self):
        # use up all questions in both rounds
        for round_num in xrange(2):
            for cat_num in xrange(self.game_state.board.MAX_CATS):
                for _ in xrange(self.game_state.board.MAX_QS):
                    self.game_state.board.mark_q_used(round_num, cat_num)

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

    def test_end_of_turn_fires_events(self):
        self.game_state.end_turn()
        self.assertTrue(self.events.did_broadcast('game_state.turn_will_end'))
        self.assertTrue(self.events.did_broadcast('game_state.turn_did_end'))
        self.assertTrue(self.events.did_broadcast('game_state.current_player_did_change'))

class TestSpin(GameStateTestCase):
    def test_spin_decrements_spins_remaining(self):
        self.assertEqual(self.game_state.spins_remaining, 50)
        self.game_state.spin()
        self.assertEqual(self.game_state.spins_remaining, 49)

    def test_spin_fires_game_end_event(self):
        self.game_state.spins_remaining = 1
        self.game_state.current_round = 2
        self.game_state.spin()
        self.assertTrue(self.events.did_broadcast('game_state.game_did_end'))

    def test_spin_fires_spin_update_event(self):
        self.game_state.spin()
        self.assertTrue(self.events.did_broadcast('game_state.spins_did_update'))

    def test_spin_fires_sector_events(self):
        self.game_state.spin()
        self.assertTrue(self.events.did_broadcast('game_state.sector_was_chosen'))

class TestEndGame(GameStateTestCase):
    def test_game_end_when_no_more_questions(self):
        self.assertFalse(self.game_state.has_game_ended())
        self.use_all_questions()
        self.game_state.current_round = 2
        self.assertTrue(self.game_state.has_game_ended())

    def test_round_end_when_no_more_spins(self):
        self.assertFalse(self.game_state.has_round_ended())
        self.game_state.spins_remaining = 0
        self.assertTrue(self.game_state.has_round_ended())

    def test_game_end_when_no_more_spins_or_questions(self):
        self.assertFalse(self.game_state.has_game_ended())
        self.game_state.spins_remaining = 0
        self.game_state.current_round = 2
        self.use_all_questions()
        self.assertTrue(self.game_state.has_game_ended())

if __name__ == '__main__':
    unittest.main()
