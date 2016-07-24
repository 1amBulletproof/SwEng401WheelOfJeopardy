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
    def __init__(self):
        #2d array of questions, with 5 rows and 6 columns
        #there are 6 different categories of questions
        cols = 6
        #there are 5 questions in each category
        rows = 5
        #this matrix is filled with default Questions.. EDIT?
        #John created a script that will read questions in from
        #an input file.
        #12 lists of questions - 2 rounds of 6 categories
        questions = [[Question() for j in range(cols)]
                          for i in range(rows)]

    #return the question at location r, c (row, column)
    def get(r, c):
        return questions[r][c]

    #load contents - didn't John write this?
    def load(contents)
    # @TODO: replace with correct logic

    #load file of questions - didn't John write this?
    def load_file(path)
    # @TODO: replace with correct logic

"""
    #needed? probably not..
    def remove_question(self):
        # @TODO: replace with correct logic

    def get_question_category(self):
        # @TODO: replace with correct logic
        #get question column
        #get the category value from the category array

    #needed? probably not...
    def set_question_category(column):
        # @TODO: replace with correct logic
        #set the category for a column
"""
