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
    #I think we need to pass in the current round also - Victoria
    #this will allow us to assign the correct # of daily doubles
    def __init__(self, catgs, Qs, pts):
        self.headers = catgs
        self.questions = Qs
        self.pointValue = pts
        
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

        #set the daily double questions
        set_daily_double_pos(self)

    #generate random daily double position in the matrix
    def set_daily_double_pos(self):
        #insert logic for determining 1st or 2nd round
        randCol = random.randrange(0, len(self.headers))
        randRow = random.randrange(0, len(self.questions))
        self.questions[randRow][randCol].set_daily_double()
        #if 2nd round, do this again
    
    #return the tuple of (pointValue, Category, Question)
    #stored at location c, r (column, row)
    def get(c, r):
        catg = self.headers[c]
        val = self.pointValue[r]
        return (val, catg, questions[r][c])

    def get_value(r):
        """
        Get the point value of the n-th question in the round.
        """
        return self.pointValue[r]

    def __str__(self):
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
    def __init__(self, questionText, answer):
        self.text = questionText
        self.answer = answer
        #default to False - will be assigned from the matrix
        self.daily_double = False #is question a daily double

    # get question text
    def get_question(self):
        return self.text

    # get answer
    def get_answer(self):
        return self.answer

    #get daily double status
    def is_daily_double(self):
        return self.daily_double

    #set daily double status to true(called from QuestionMatrix)
    def set_daily_double(self):
        self.daily_double = True

    # string representation
    def __str__(self):
        return self.text + " : " + self.answer
        
    #def __repr__(self):
    #	return 'Qu:self.__str__()""'
