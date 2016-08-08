"""
Sector Super Class

action() method MUST be overriden by sub-classes
"""

#@TODO: unit tests for class
class Sector:
    def __init__(self, name):
        self.name = name

    def action(self, game_state):
        raise NotImplementedError

    def __str__(self):
        return self.name

    def process_question(self, game_state):
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


        """
        Methods to deal with answering question for board_sector,
        player_choice_sector & opponent_choice_sector
        """
    def receive_answer(self, game_state, question, answer):
        game_state.events.broadcast('board_sector.check_answer', question, answer)

    def received_correct_answer(self, game_state, question):
        game_state.get_current_player().increase_score_by(question[0])
        game_state.end_turn()

    def received_incorrect_answer(self, game_state, question):
        game_state.get_current_player().decrease_score_by(question[0])
        # @TODO: use free token?
        game_state.end_turn()
