# -*- coding: utf-8 -*-

from wheelofjeopardy.utils.read_question_file import read_questions
import os

"""
Controls and monitors the state of the Questions/Board
From SRS document:
...is responsible for selecting, displaying, or tracking
which questions have already been selected.
"""

class QuestionBoardState(object):
    def __init__(self, events, opts):
        self.events = events
        self.MAX_QS = 5 # max questions per category
        self.MAX_CATS = 6 # max categories per round

        #two question_matrix returned - 1 for each round
        (tmp1, tmp2) = read_questions(opts) # read questions

        #the question matrix, 2 question_matrix (1 for each round)
        self._q_mat = [tmp1, tmp2]

        #list of int to keep track of question progress
        self.progress = [[0 for x in range(self.MAX_CATS)] for y in range(2)]
        self.progress[0][0] = 4
        self.visuals = self._get_board_visuals() # for visualizing boards

    def q_remaining(self, round_num):
        """
        Number of questions remaining in a round

        @type    roundNum: int
        @param   roundNum: The round number (1 = round one, etc)

        @rtype:  int
        @return: the number of questions remaining in said round
        """
        return (self.MAX_QS * self.MAX_CATS) - sum(self.progress[round_num - 1])

    def no_q_in_round(self, round_num):
        """
        Whether there are remaining questions in a round

        @type    roundNum: int
        @param   roundNum: The round number (1 = round one, etc)

        @rtype:  boolean
        @return: True if no more questions remains in round, False otherwise
        """
        return (self.q_remaining(round_num) == 0)

    def mark_q_used(self, round_num, catg_num):
        """
        Marks a question on the board as used

        @type    roundNum: int
        @param   roundNum: The round number (1 = round one, etc)

        @type    catgNum: int
        @param   catgNum: The category number (1 = first category, etc)
        """
        if self.progress[round_num - 1][catg_num - 1] < self.MAX_QS:
            # increment the progress count if still question left in category
            self.progress[round_num - 1][catg_num - 1] += 1

    def mark_all_q_used(self, round_num):
        self.progress[round_num - 1][:] = [self.MAX_QS] * self.MAX_CATS

    def next_q_in_category(self, round_num, catg_num):
        """
        Returns the next question in the given category

        @type    roundNum: int
        @param   roundNum: The round number (1 = round one, etc)

        @type    catgNum: int
        @param   catgNum: The category number (1 = first category, etc)

        @rtype:  Question
        @return: next QuestionWithMetadata in the category given
        """
        next_idx = self.progress[round_num - 1][catg_num - 1] # get idx before marking
        self.mark_q_used(round_num, catg_num) # note: mark_q_used is 1-indexed
        return self._q_mat[round_num - 1].get(catg_num - 1, next_idx)

    def num_q_left_in_category(self, round_num, catg_num):
        """
        Returns the number of questions left in a given category

        @type    roundNum: int
        @param   roundNum: The round number (1 = round one, etc)

        @type    catgNum: int
        @param   catgNum: The category number (1 = first category, etc)

        @rtype:  int
        @return: number of unused in the given round and category
        """
        return (self.MAX_QS - self.progress[round_num - 1][catg_num - 1])

    def get_catg_status(self, round_num, catg_num):
        """
        Returns the status of the category (are all questions
        answered or not?)

        @type    roundNum: int
        @param   roundNum: The round number (1 = round one, etc)

        @type    catgNum: int
        @param   catgNum: The category number (1 = first category, etc)

        @rtype:  boolean
        @return: true if there are questions remaining in the category
        """
        return (self.num_q_left_in_category(round_num, catg_num) > 0)

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
        cats = self._q_mat[self._current_round() - 1].headers
        out_str = ''

        for n in range(len(cats)):
            out_str += ('\t' + '(' + str(n + 1) + ') ' + cats[n] + '\n')

        return out_str

    def _get_board_visuals(self):
        if os.name == 'nt':
            return [' X ', ' O ', '-']
        else:
            return [' ✕ ', ' ○ ', '¯']

    def _get_board_q_status(self):
        mat = [None for x in range(self.MAX_CATS)]
        r = self._current_round()

        for n in range(self.MAX_CATS):
            used = self.progress[r - 1][n] # progress is 0-indexed
            rem = self.MAX_QS - used
            mat[n] = [False for x in range(used)] + [True for y in range(rem)]

        return map(list, zip(*mat)) # tranposed

    def __str__(self):
        vz = self.visuals # to be used in printing
        r = self._current_round()
        out_str = 'Current Round: %u\n' % r
        out_str += 'Categories:\n' + self.get_categories()

        out_str += '_' * (self.MAX_CATS * 4 + 1) + '\n' # top bar
        cats = range(1, self.MAX_CATS + 1)
        out_str += '|(' + ')|('.join(map(str, cats)) + ')|\n'
        out_str += '-' * (self.MAX_CATS * 4 + 1) + '\n' # bar between catgs and mat
        mat = [None for x in range(self.MAX_CATS)]

        for n in range(self.MAX_CATS):
            used = self.progress[r - 1][n] # progress is 0-indexed
            rem = self.MAX_QS - used
            mat[n] = [vz[0] for x in range(used)] + [vz[1] for y in range(rem)]

        mat = map(list, zip(*mat)) # transpose the progress matrix
        tmp = map(lambda x: '|' + '|'.join(x) + '|', mat) # create line output
        out_str += '\n'.join(tmp) + '\n' # all table lines
        out_str += vz[2] * (self.MAX_CATS * 4 + 1) # bottom bar

        return out_str
