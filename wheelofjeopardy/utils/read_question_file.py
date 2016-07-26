# -*- coding: utf-8 -*-
"""
Read and parse question file (CSV) and return a QuestionMatrix object containing
the questions. Also performs basic error checking. The question file does not
need to be in listed in particular order, but does need to satisfy all the
formatting requirements for questions. See README

@author: J Wu, johnwuy@gmail.com
"""

#%% Auxiliary function section
trueList = set(['TRUE', '1', 'T', 'Y'])

# to index entire row in 2D-List
def sliceCol( mat, col):
    return [row[col] for row in mat]

# return all index of an element in list
def indexAll( l, elem):
    return [ind for ind,x in enumerate(l) if x==elem]

# parse each CSV row, return value
def getDataFromQRow(row):
    (rdInd, pts) = map(int, (row['Rounds'], row['Points']) ) # conv str to int
    dd = row['DailyDouble'].upper() in trueList # if in set of true strings
    return (rdInd, row['Category'], pts, row['Question'], row['Answer'], dd)


#%% Read CSV
def ReadQuestions(opts):
    import os, csv, sys
    import wheelofjeopardy.question_matrix as qm

    numQs = 5 # number of questions in category
    numCats = 6 # number of categories per round

    #d = os.path.dirname(os.path.realpath(sys.argv[0]))
    inFileName = opts.qFileName
    fPath = os.path.join(os.getcwd(), "wheelofjeopardy", 'cfg', inFileName)

#%% Parse CSV line-by-line and instantiate the various questions

    catgInd1 = dict() # dict to keep list indices for round 1 categories
    catgInd2 = dict() # dict to keep list indices for round 2 categories
    # the following 2D-list are to store questions for round 1 and 2
    qsRd1 = [[None for x in range(numQs)] for y in range(numCats)]
    qsRd2 = [[None for x in range(numQs)] for y in range(numCats)]

    with open(fPath, 'r') as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            (rdInd, cat, pts, qTxt, ans, dd) = getDataFromQRow(row) # read row

            if rdInd == 1:
                if not catgInd1.has_key(cat): # if category not encountered yet
                    catgInd1[cat] = len(catgInd1) # designate new index
                # instantiate questions
                qsRd1[catgInd1[cat]][pts-1] = qm.Question(qTxt, ans) 

            elif rdInd == 2:
                if not catgInd2.has_key(cat):
                    catgInd2[cat] = len(catgInd2)
                # instantiate questions
                qsRd2[catgInd2[cat]][pts-1] = qm.Question(qTxt, ans)

            else: # do nothing with final jeopardy for now
                pass

#%% Instantiate QuestionMatrix method, check for consistency, and return
# TODO(J Wu) implement this once we get class functions

    # prepare categories
    catgRound1 = [None for x in range(numCats)]
    catgRound2 = [None for x in range(numCats)]
    for key,val in catgInd1.iteritems():
        catgRound1[val] = key
    for key,val in catgInd2.iteritems():
        catgRound2[val] = key

    # Instantiate two QuestionMatrix objects
    qMat1 = qm.QuestionMatrix(catgRound1, qsRd1, opts.qPoints1)
    qMat2 = qm.QuestionMatrix(catgRound2, qsRd2, opts.qPoints2)

    return (qMat1, qMat2)
