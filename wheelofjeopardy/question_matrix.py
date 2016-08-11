import random

class QuestionMatrix(object):
    """
    Controls and monitors the Question Matrix


    From SRS document:
    It is worth noting that the question matrix itself
    is not responsible for selecting, displaying, or tracking
    which questions have already been selected. Such tasks are
    the responsibility of the board submodule. The question matrix
    will store the category of the questions and contain references
    to the full body of questions in each game. The question objects
    themselves will contain the question text as well as the correct
    answer.
    """
    def __init__(self, catgs, Qs, pts):
        self.headers = catgs
        self.questions = Qs
        self.pointValues = pts

        # sanity check: number of columns
        if len(self.headers) != len(self.questions):
            raise TypeError('Check the dimension of the questions')
        else:
            self.cols = len(self.headers)
        # sanity check: number of rows
        tmp = map(len, self.questions)
        if tmp[1:] != tmp[:-1]:
            raise TypeError('Check the dimensions of the questions')
        else:
            self.rows = tmp[0]

    def get(self, c, r):
        """
        get the tuple of (pointValue, Category, Question)
        from the given location in the matrix

        @type    c: int
        @param   c: the category index # of the matrix
        @type    r: int
        @param   r: the question index # of the matrix

        @rtype:  int, string, Question
        @return: QuestionWithMetadata instance
        """
        if c < len(self.questions) and r < len(self.questions[c]):
            catg = self.headers[c]
            val = self.pointValues[r]
            return QuestionWithMetadata(self.questions[c][r], val, catg)
        else:
            return None

    def __str__(self):
        """
        get the string version of the matrix
        """
        catg = 'categories: ' + self.headers.__str__()
        strOut = '';

        # loop over questions and categories, add to strOut
        for (cat,qs) in zip(self.headers, self.questions):
            strOut += '__' + str(cat) + '__::'
            strOut += str(map(str,qs))
            strOut += '\n'

        return strOut


class Question(object):
    """
    Question Class, represents a question of WoJ
    Must be instantiated with the question text and the answer.
    @author J Wu, johnwuy@gmail.com
    """
    def __init__(self, questionText, answer, dailyDouble=False):
        self.text = questionText
        self.answer = answer
        self.daily_double = dailyDouble # is question a daily double (def=no)

    #get daily double status
    def is_daily_double(self):
        return self.daily_double

    # string representation
    def __str__(self):
        return self.text + " : " + self.answer

class QuestionWithMetadata(object):
    def __init__(self, question, point_value, category_header):
        self.question = question
        self.point_value = point_value
        self.category_header = category_header

    @property
    def text(self):
        return self.question.text

    @property
    def answer(self):
        return self.question.answer

    @property
    def daily_double(self):
        return self.question.is_daily_double()

    def is_daily_double(self):
        return self.question.is_daily_double()

    def __str__(self):
        return self.question.__str__()
