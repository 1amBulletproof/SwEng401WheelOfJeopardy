"""
Logic for player landing on any "normal" board sector of Wheel
"""
#@todo unit tests
from wheelofjeopardy.sectors.sector import Sector

class BoardSector(Sector):
    def __init__ (self, category):
        Sector.__init__(self, str(category) + " Board sector")
        self.category = category

    def action(self, game_state):
        game_state.current_category = self.category
        game_state.current_question = game_state.next_question_in_category(self.category)

        # if no question was available in the selected category...
        if game_state.current_question == None:
            # ... and the round or game has ended, end the turn
            # otherwise, don't end the turn and the player will be prompted
            # to spin again
            if game_state.has_round_ended() or game_state.has_game_ended():
                game_state.end_turn()
        else:
            game_state.events.broadcast(
                'board_sector.question_will_be_asked', game_state.current_question
            )

    def receive_answer(self, game_state, question, answer):
        game_state.events.broadcast('board_sector.check_answer', question, answer)

    def received_correct_answer(self, game_state, question):
        game_state.get_current_player().increase_score_by(question[0])
        game_state.end_turn()

    def received_incorrect_answer(self, game_state, question):
        game_state.get_current_player().decrease_score_by(question[0])
        # @TODO: use free token?
        game_state.end_turn()
