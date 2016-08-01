# -*- coding: utf-8 -*-

"""
Controls and monitors the state of the Questions/Board
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
        
        #the question matrix
        self.q_mat = [tmp1, tmp2]

        #list of int to keep track of question progress
        self.progress = [[0 for x in range(self.MAX_CATS)] for y in range(2)]

        """
        #list of category statuses - 1 means the category
        #still has questions, 0 means all questions have been
        #used
        """
        self.catgs_statuses = [1 1 1 1 1 1]

        
    def q_remaining(self, roundNum):
        """
        Number of questions remaining in a round

        @type    roundNum: int
        @param   roundNum: The round number (1 = round one, etc)

        @rtype:  int
        @return: the number of questions remaining in said round
        """
        return sum(self.progress[roundNum-1])

    def no_q_in_round(self, roundNum):
        return (self.q_remaining(roundNum) > 0)

    # this may be redundant, as can use _current_round() == 3
    def no_more_q(self):
        return (self.no_q_in_round(1) and self.no_q_in_round(2))

    def mark_q_used(self, roundNum, catgNum):
        if self.progress[roundNum-1][catgNum-1] < self.MAX_QS:
            # increment the progress count if still question left in category
            self.progress[roundNum-1][catgNum-1] += 1
        else:
            catgs_statuses[catgNum-1] = 0 #set the catg status to 0
            raise RuntimeWarning('No more questions in category.')

    def next_q_in_category(self, roundNum, catgNum):
        # not sure if I should mark question as used automatically after get
        mark_q_used(self, roundNum-1, catgNum-1)
        return self.q_mat[roundNum-1][catgNum-1]

    def _current_round(self):
        if self.no_q_in_round(1):
            if self.no_q_in_round(2):
                return 3
            else:
                return 2
        else:
            return 1

    def get_categories(self):
        cats = self.q_mat[self._current_round()].headers
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

