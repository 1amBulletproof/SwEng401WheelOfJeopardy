# -*- coding: utf-8 -*-
"""
Read and parse question file (CSV) and return a QuestionMatrix object containing
the questions. Also performs basic error checking. The question file does not
need to be in listed in particular order, but does need to satisfy all the
formatting requirements for questions. See README.

@author: J Wu, johnwuy@gmail.com
"""

#%% Auxiliary function section
true_list = set(['TRUE', '1', 'T', 'Y'])

# to index entire row in 2D-List
def slice_col( mat, col):
    return [row[col] for row in mat]

# return all index of an element in list
def index_all( l, elem):
    return [ind for ind,x in enumerate(l) if x == elem]

# parse each CSV row, return value
def get_data_from_q_row(row):
    (rd_ind, pts) = map(int, (row['Rounds'], row['Points']) ) # conv str to int
    if opts.daily_double:
        dd = row['DailyDouble'].upper() in true_list # if in set of true strings
    else:
        dd = False

    return (rd_ind, row['Category'], pts, row['Question'], row['Answer'], dd)


#%% Read CSV
def read_questions(inOpts):
    import os, csv, sys
    import wheelofjeopardy.question_matrix as qm
    global opts # make opts readable from util functions
    opts = inOpts

    num_qs = 5 # number of questions in category
    num_cats = 6 # number of categories per round

    #d = os.path.dirname(os.path.realpath(sys.argv[0]))
    in_file_name = opts.q_file_name
    f_path = os.path.join(os.getcwd(), 'wheelofjeopardy', 'cfg', in_file_name)

#%% Parse CSV line-by-line and instantiate the various questions

    catg_ind1 = dict() # dict to keep list indices for round 1 categories
    catg_ind2 = dict() # dict to keep list indices for round 2 categories
    # the following 2D-list are to store questions for round 1 and 2
    qs_rd1 = [[None for x in range(num_qs)] for y in range(num_cats)]
    qs_rd2 = [[None for x in range(num_qs)] for y in range(num_cats)]

    with open(f_path, 'r') as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            (rd_ind, cat, pts, q_txt, ans, dd) = get_data_from_q_row(row) # row

            if rd_ind == 1:
                if not catg_ind1.has_key(cat): # if category not encountered yet
                    catg_ind1[cat] = len(catg_ind1) # designate new index
                # instantiate questions
                qs_rd1[catg_ind1[cat]][pts - 1] = qm.Question(q_txt, ans, dd)

            elif rd_ind == 2:
                if not catg_ind2.has_key(cat):
                    catg_ind2[cat] = len(catg_ind2)
                # instantiate questions
                qs_rd2[catg_ind2[cat]][pts - 1] = qm.Question(q_txt, ans, dd)

            else: # do nothing with final jeopardy for now
                pass

#%% Instantiate QuestionMatrix method, check for consistency, and return
    # prepare categories
    catg_round1 = [None for x in range(num_cats)]
    catg_round2 = [None for x in range(num_cats)]

    for key, val in catg_ind1.iteritems():
        catg_round1[val] = key

    for key, val in catg_ind2.iteritems():
        catg_round2[val] = key

    # Instantiate two QuestionMatrix objects
    q_mat1 = qm.QuestionMatrix(catg_round1, qs_rd1, opts.q_points1)
    q_mat2 = qm.QuestionMatrix(catg_round2, qs_rd2, opts.q_points2)

    return (q_mat1, q_mat2)
