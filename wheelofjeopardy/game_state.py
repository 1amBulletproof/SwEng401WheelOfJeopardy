from wheelofjeopardy.question_board_state import QuestionBoardState
from wheelofjeopardy.wheel import Wheel

class GameState(object):
  TOTAL_SPINS = 50

  def __init__(self, player_states):
    self.spins_remaining = GameState.TOTAL_SPINS
    self.player_states = player_states
    self.current_player_index = 0
    self.board = QuestionBoardState()
    self.wheel = Wheel()

  def get_current_player(self):
    return self.player_states[self.current_player_index]

  def any_spins_remaining(self):
    return self.spins_remaining > 0

  def spin(self):
    sector = self.wheel.spin()
    sector.apply_to(self)
    self.spins_remaining -= 1

  def end_turn(self):
    self.choose_next_player()

  def has_game_ended(self):
    return (not self.board.any_questions_remaining()) or (not self.any_spins_remaining())

  # private

  def choose_next_player(self):
    if self.current_player_index == len(self.player_states) - 1:
      self.current_player_index = 0
    else:
      self.current_player_index += 1
