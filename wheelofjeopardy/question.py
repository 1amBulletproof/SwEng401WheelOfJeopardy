'''
question.py encompasses the Question class, needs to be supplied its question and
correct answer from QuestionMatrix which calls read_question_file.py.

@author = Miranda Link, mirandanlink@gmail.com
'''

# Imports
#

# define Question Class
#
class Question(object):
	def __init__(self, question, correctAnswer, dailyDouble=False):
		self.question = question
		self.correctAnswer = correctAnswer
		self.dailyDouble = dailyDouble

	# receive submitted answer from player
	#
	def answerCorrect(self, submittedAnswer):
		# compare to correct answer
		#
		return submittedAnswer == self.correctAnswer