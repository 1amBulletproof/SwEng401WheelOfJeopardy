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

John has written a script that will create 12 lists of questions
2 rounds * 6 categories of questions = 12 lists

reader returns an instance of question matrix

has a load file method

"""
#need an import statement from question class?
#from wheelofjeopardy.question import Question

class QuestionMatrix(object):
    def __init__(self, catgs, Qs, pts):
        #2d array of questions, with 5 rows and 6 columns
        #there are 6 different categories of questions
        cols = 6
        #there are 5 questions in each category
        rows = 5
        #this matrix is filled with default Questions.. EDIT?
        #John created a script that will read questions in from
        #an input file.
        #12 lists of questions - 2 rounds of 6 categories
        self.categories = catgs
        self.questions = Qs
        self.pointValue = pts


    #return the tuple of (pointValue, Category, Question)
    #stored at location r, c (row, column)
    def get(r, c):
        catg = categories[c]
        val = pointValue[c]
        return (val, catg, questions[r][c])


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

