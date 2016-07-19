"""
Controls and monitors the state of the Questions/Board
"""
class QuestionBoardState(object):
    def __init__(self):
        # @TODO: replace with correct logic
        self.questions_remaining = 30

    def any_questions_remaining(self):
        # @TODO: replace with correct logic
        return self.questions_remaining > 0
