"""
Controls and monitors the state of the Questions/Board
Initial author: Victoria Scalfari
From SRS document:
...is responsible for selecting, displaying, or tracking
which questions have already been selected.
"""
class QuestionBoardState(object):
    def __init__(self, events, Opts):
        from wheelofjeopardy.utils.read_question_file import ReadQuestions
        self.events = events
        self.MAX_QS = 5 # max questions per category
        self.MAX_CATS = 6 # max categories per round		

        (tmp1,tmp2) = ReadQuestions(Opts) # read questions
        q_mat = [tmp1, tmp2]

        #list of int to keep track of question progress
        self.progress = [[0 for x in range(self.MAX_CATS)] for y in range(2)]

    def q_remaining(self, roundNum):
        """
        Number of questions remaining in a round

        @type    roundNum: int
        @param   roundNum: The round number (1 = round one, etc)

        @rtype:  int
        @return: the number of questions remaining in said round
        """
        return sum(self.progress[roundNum-1])

    def no_q_in_round(self, roudNum):
        return (q_remaining(roundNum) > 0)

    def no_more_q(self):
        return (no_q_in_round(1) and no_q_in_round(2))


    def mark_q_used(self, roundNum, catgNum):
        if self.progress[roundNum-1][catgNum-1] < self.MAX_QS:
            # increment the progress count if still question left in category
            self.progress[roundNum-1][catgNum-1] += 1
        else:
            raise RuntimeWarning('No more questions in category.')


    def next_in_category(roundNum, catgNum):
        # not sure if I should mark question as used automatically after get
        return q_mat[roundNum-1][catgNum-1]
