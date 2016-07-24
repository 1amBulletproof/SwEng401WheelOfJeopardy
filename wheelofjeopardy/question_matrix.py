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
2 rounds * 6 categories of questions

reader returns an instance of question matrix

has a load file method

"""
class QuestionMatrix(object):
    def __init__(self):
        #2d array of questions, with 5 rows and 6 columns
        rows = 5
        cols = 6
        #this matrix is filled with default Questions.. EDIT?
        #are we reading questions in from a file? Or generating them
        #in the question class?
        #12 lists of questions
        questionMatrix = [[Question() for j in range(cols)] for i in range(rows)]

    #find and return the row, column of the given element in matrix l
    def find(l, elem):
        for row, i in enumerate(l):
            try:
                column = i.index(elem)
            except ValueError:
                continue
            return row, column
        return -1

    #replace a given old question with a new question
    def replace_question(oldQuestion, newQuestion):
        # @TODO: replace with correct logic

        #find the old question in the question matrix
        #the find method returns the row, column of the oldQuestion
        row, column = find(questionMatrix, oldQuestion)
        questionMatrix[row, column] = newQuestion

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
