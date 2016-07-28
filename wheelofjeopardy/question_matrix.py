class QuestionMatrix(object):
    """
    Controls and monitors the Question Matrix
    Initial Author: Victoria


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
        #there are 6 different categories of questions
        cols = 6
        #there are 5 questions in each category
        rows = 5
        self.categories = catgs
        self.questions = Qs
        self.pointValue = pts
        
        # sanity check
        if (not len(self.categories)==6) or (not len(self.questions)==6):
            raise TypeError('Check the dimension of the questions')
        if not( map(len, self.questions)==[5 for x in range(6)]):
            raise TypeError('Check the dimensions of the questions')


    #return the tuple of (pointValue, Category, Question)
    #stored at location r, c (row, column)
    def get(r, c):
        catg = categories[c]
        val = pointValue[c]
        return (val, catg, questions[r][c])

    def __str__(self):
        catg = 'Categories: ' + self.categories.__str__()
        strOut = '';
        
        # loop over questions and categories, add to strOut
        for (cat,qs) in zip(self.categories, self.questions): 
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

    # get question text
    def getQuestion(self):
        return self.text

    # get answer
    def getAnswer(self):
        return self.answer

    # string representation
    def __str__(self):
        return self.text + " : " + self.answer
        
    #def __repr__(self):
    #	return 'Qu:self.__str__()""'
