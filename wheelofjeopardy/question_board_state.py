# -*- coding: utf-8 -*-

from wheelofjeopardy.utils.read_question_file import ReadQuestions

"""
Controls and monitors the state of the Questions/Board
From SRS document:
...is responsible for selecting, displaying, or tracking
which questions have already been selected.
"""

class QuestionBoardState(object):
    def __init__(self, events, Opts):
        self.events = events
        self.MAX_QS = 5 # max questions per category
        self.MAX_CATS = 6 # max categories per round

        #two question_matrix returned - 1 for each round
        (tmp1,tmp2) = ReadQuestions(Opts) # read questions

        #the question matrix
        #2 question_matrix (1 for each round)
        self._q_mat = [tmp1, tmp2]

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
        return (self.MAX_QS*self.MAX_CATS) - sum(self.progress[roundNum-1])

    def no_q_in_round(self, roundNum):
        """
        Whether there are remaining questions in a round

        @type    roundNum: int
        @param   roundNum: The round number (1 = round one, etc)

        @rtype:  boolean
        @return: True if no more questions remains in round, False otherwise
        """
        return (self.q_remaining(roundNum) == 0)

    def no_more_q(self):
        """
        Whether there are any more questions left in the game

        @rtype:  boolean
        @return: true if the round # is > 2
        """
        return self._current_round() > 2 # round = 3 means first 2 round is over

    def mark_q_used(self, roundNum, catgNum):
        """
        Marks a question on the board as used

        @type    roundNum: int
        @param   roundNum: The round number (1 = round one, etc)

        @type    catgNum: int
        @param   catgNum: The category number (0 = first category, etc)
        """
        if self.progress[roundNum-1][catgNum-1] < self.MAX_QS:
            # increment the progress count if still question left in category
            self.progress[roundNum-1][catgNum-1] += 1
        else:
            raise RuntimeWarning('No more questions in category.')

    def next_q_in_category(self, roundNum, catgNum):
        """
        Returns the next question in the given category

        @type    roundNum: int
        @param   roundNum: The round number (1 = round one, etc)

        @type    catgNum: int
        @param   catgNum: The category number (0 = first category, etc)

        @rtype:  Question
        @return: next Question in the category given
        """
        self.mark_q_used(roundNum-1, catgNum-1)
        next_idx = self.progress[roundNum-1][catgNum-1]
        return self._q_mat[roundNum-1].get(catgNum-1, next_idx)

    def no_q_in_category(self, roundNum, catgNum):
        """
        Returns the number of questions left in a given category

        @type    roundNum: int
        @param   roundNum: The round number (1 = round one, etc)

        @type    catgNum: int
        @param   catgNum: The category number (0 = first category, etc)

        @rtype:  int
        @return: number of questions in the given category
        """
        return (self.progress[roundNum-1][catgNum-1])

    def get_catg_status(self, roundNum, catgNum):
        """
        Returns the status of the category (are all questions
        answered or not?)

        @type    roundNum: int
        @param   roundNum: The round number (1 = round one, etc)

        @type    catgNum: int
        @param   catgNum: The category number (0 = first category, etc)

        @rtype:  boolean
        @return: true if there are questions remaining in the category
        """
        return (self.progress[roundNum-1][catgNum-1] < self.MAX_QS)

    def _current_round(self):
        """
        Returns the current round

        @rtype:  int
        @return: 1 if 1st round, 2 if 2nd round, 3 if game over
        """
        if self.no_q_in_round(1):
            if self.no_q_in_round(2):
                return 3
            else:
                return 2
        else:
            return 1

    def get_categories(self):
        """
        Returns the categories string

        @rtype:  String
        @return: the string of all categories in the game
        """
        cats = self._q_mat[self._current_round()-1].headers
        outStr = ''
        for n in range(len(cats)):
            outStr += ('\t' + '(' + str(n+1) + ') ' + cats[n] + '\n')
        return outStr

    def __str__(self):
        r = self._current_round()
        outStr = 'Current Round: %u\n' % r
        outStr += 'Categories:\n' + self.get_categories()

        outStr += '_' * (self.MAX_CATS*4+1) + '\n' # top bar
        cats = range(1, self.MAX_CATS+1)
        outStr += '|(' + ')|('.join( map(str,cats) ) + ')|\n'
        outStr += '-' * (self.MAX_CATS*4+1) + '\n' # bar between catgs and mat
        mat = [None for x in range(self.MAX_CATS)]
        for n in range(self.MAX_CATS):
            used = self.progress[r][n]
            rem = self.MAX_QS - used
            mat[n] = [' ✕ ' for x in range(used)] + [' ○ ' for y in range(rem)]
        mat = map(list, zip(*mat)) # transpose the progress matrix
        tmp = map(lambda x: '|' + '|'.join(x) + '|', mat) # create line output
        outStr += '\n'.join(tmp) + '\n' # all table lines
        outStr += '¯' * (self.MAX_CATS*4+1) # bottom bar
        return outStr
