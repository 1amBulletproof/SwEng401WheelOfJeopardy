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

    def ask_next_question_in_category(self, category, game_state):
        game_state.current_question = game_state.next_question_in_category(category)

        # if no question was available in the selected category...
        if game_state.current_question != None:
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

    def received_incorrect_answer(self, game_state, question):
        game_state.get_current_player().decrease_score_by(question[0])
        # @TODO: use free token?
        game_state.end_turn()
