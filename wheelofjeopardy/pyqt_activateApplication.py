'''
This is a class that can be called to bring up the wojApplication gui.

@author = Miranda Link, mirandanlink@gmail.com
'''


# imports
#
import wojApplication

# define wojApplication class
#
class ActivateWojApplication(QMainWindow, WojApplication.Ui_WojApplication):
	def __init__(self, parent=None):
		super(ActivateWojApplication, self).__init__(parent)
		self.setupUi(self)

		# initialize variables - i.e. set up the entire board... ugh
		#
		boardPopulation(categories, questions, answers, self)
		self.category1.setText(category1)

	# Methods that run on specific button clicks
	#
	@pyqtSignature("")
	def on_spinButton_clicked(self):
		# do cool things with the "wheel"
		#

		# animation

		# or randomize number between 0 and 12 and return

	@pyqtSignature("")
	def on_submitAnswerButton_clicked(self):
		# bring up moderator popup
		#

def boardPopulation(categories, questions, answers, self):
	# somehow get all of the things the board needs to display
	#

	# configure Jeopardy board.
	#
	self.category1.setText()
	self.category1Cell1.setText()
	self.category1Cell2.setText()
	self.category1Cell3.setText()
	self.category1Cell4.setText()
	self.category1Cell5.setText()
	self.category1Cell6.setText()
	self.category2.setText()
	self.category2Cell1.setText()
	self.category2Cell2.setText()
	self.category2Cell3.setText()
	self.category2Cell4.setText()
	self.category2Cell5.setText()
	self.category2Cell6.setText()
	self.category3.setText()
	self.category3Cell1.setText()
	self.category3Cell2.setText()
	self.category3Cell3.setText()
	self.category3Cell4.setText()
	self.category3Cell5.setText()
	self.category3Cell6.setText()
	self.category4.setText()
	self.category4Cell1.setText()
	self.category4Cell2.setText()
	self.category4Cell3.setText()
	self.category4Cell4.setText()
	self.category4Cell5.setText()
	self.category4Cell6.setText()
	self.category5.setText()
	self.category5Cell1.setText()
	self.category5Cell2.setText()
	self.category5Cell3.setText()
	self.category5Cell4.setText()
	self.category5Cell5.setText()
	self.category5Cell6.setText()

	# configure today's contestants
	#
	self.player1Name.setText()
	self.player1Score.setText()
	self.player2Name.setText()
	self.player2Score.setText()
	self.player3Name.setText()
	self.player3Score.setText()