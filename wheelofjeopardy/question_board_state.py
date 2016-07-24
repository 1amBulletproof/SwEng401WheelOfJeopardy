"""
Controls and monitors the state of the Questions/Board
Initial author: Victoria Scalfari
From SRS document:
...is responsible for selecting, displaying, or tracking
which questions have already been selected.
"""
class QuestionBoardState(object):
    def __init__(self, events):
        self.events = events

        # @TODO: replace with correct logic
        self.questions_remaining = 30

    def any_questions_remaining(self):
        # @TODO: replace with correct logic
        return self.questions_remaining > 0

    def mark_question_used(self):
        if any_questions_remaining():
            self.questions_remaining = self.questions_remaining - 1
