# -*- coding: utf-8 -*-
"""
Read and parse question file (CSV) and return a QuestionMatrix object containing
the questions. Also performs basic error checking. The question file does not
need to be in listed in particular order, but does need to satisfy all the
formatting requirements for questions. See README

@author: J Wu, johnwuy@gmail.com
"""
# def read_question_file(inFileName):

#%% Setup and configurations
import os, csv, sys

# TODO(J Wu) once option class is done, implement use of that in this section

numQs = 5 # number of questions in category
numCats = 6 # number of categories per round

trueList = set(['TRUE', '1', 'T', 'Y'])

# d = os.path.dirname(os.path.realpath(sys.argv[0]))
inFileName = 'Questions_Aired_08Apr2011.csv'
fPath = os.path.join(os.getcwd(), 'cfg', inFileName)

#%% Auxiliary function section

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


#%% Parse CSV line-by-line and instantiate the various questions

catgRd1 = dict() # dict to keep list indices for round 1 categories
catgRd2 = dict() # dict to keep list indices for round 2 categories
# the following 2D-list are to store questions for round 1 and 2
qsRd1 = [[None for x in range(numQs)] for y in range(numCats)]
qsRd2 = [[None for x in range(numQs)] for y in range(numCats)]

with open(fPath, 'r') as csvfile:
    reader = csv.DictReader(csvfile)

    for row in reader:
        (rdInd, cat, pts, qTxt, ans, dd) = getDataFromQRow(row) # read row

        if rdInd == 1:
            if not catgRd1.has_key(cat): # if category not encountered yet
                catgRd1[cat] = len(catgRd1) # designate new index

            # put question class instantiation here
            qsRd1[catgRd1[cat]][pts-1] = qTxt +'|' +ans # placeholder for now

        elif rdInd == 2:
            if not catgRd2.has_key(cat):
                catgRd2[cat] = len(catgRd2)

            # put question class instantiation here
            qsRd2[catgRd2[cat]][pts-1] = qTxt +'|' +ans # placeholder for now

        else: # do nothing with final jeopardy for now
            pass

#%% Instantiate QuestionMatrix method, check for consistency, and return
# TODO(J Wu) implement this once we get class functions

#return (qsRd1, qsRd2)