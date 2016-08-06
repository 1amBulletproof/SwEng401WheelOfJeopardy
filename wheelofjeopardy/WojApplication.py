'''
This is a class that can be called to bring up the wojApplication gui.

@author = Miranda Link, mirandanlink@gmail.com
'''


# imports
#
import sys
sys.path.append('./gui')
import wojApplication # this is the .py file spit out from PyQt

# define wojApplication class
#
class ActivateWojApplication(QMainWindow, WojApplication.Ui_WojApplication):
	def __init__(self, events, parent=None):
		super(ActivateWojApplication, self).__init__(parent)
		self.setupUi(self)
		self.events = events

		# subscriptions
		#
		self.events.subscribe('board_sector.deactivate_square', self._deactivate_square)
		self.events.subscribe('player_choice_sector.choose_category', self._show_category_popup)
		self.events.subscribe('opponent_choice_sector.choose_category', self._show_category_popup)
		self.events.subscribe('board_sector.prompt_for_wager', self._show_daily_double_popup)
		self.events.subscribe('sector.prompt_for_token_use', self._show_token_popup)
		self.events.subscribe('bankrupt_sector.update_score', self._zero_score)
		self.events.subscribe('moderator.update_score', self._update_score)
		self.events.subscribe('game_state.spins_did_update', self._update_spin_count)
		self.events.subscribe('game_state.game_did_end', self._game_end)
		self.events.subscribe('player_state.current_player_did_change', self._set_player)

		# initialize variables - i.e. set up the entire board.
		#
		board_population(categories, question_values, self)
		contestant_population(players, self)

		# put image behind wheel
		#


		# setup the player answer interface to not show "TextLabels" everywhere.
		#
		self.sectorOutput.setText("")
		self.currentQuestion.setText("")
		self.playerAnswerLabel.setText("")


	# Methods that run on specific button clicks
	#
	@pyqtSignature("")
	def on_spinButton_clicked(self):
		# broadcast that the spin button was clicked
		#
		self.events.broadcast('spin_happened')

		# animate the wheel
		#
		pass


	@pyqtSignature("")
	def on_submitAnswerButton_clicked(self):
		# call activateModeratorPopup
		self.broadcast('gui.answer_received')
		pass


	# Functions that run from subscriptions
	#
	def _deactivate_square(self, square):
		# when a square's question has been shown to the user
		#
		self.square.setEnabled(False)


	def _game_end(self):
		pass


	def _set_player(self):
		# set the current player for the answer area
		#
		self.playerAnswerLabel.setText(current_player)

		# bold the current player in the player area
		#
		self.playerName.setFont.setBold(True)
		pass

	def _show_category_popup(self):
		# call activateCategoryPopup
		#
		pass


	def _show_daily_double_popup(self):
		# call activateDailyDoublePopup
		pass


	def _show_token_popup(self):
		# call activateTokenPopup
		pass


	def _update_score(self):
		# needs to know current player..
		#
		current_score = self.playerScore.text()
		new_score = int(current_score) + question_point_value
		self.playerScore.setText(new_score)
		pass

	def _update_spin_count(self):
		count = self.spinCountLabel.text()
		new_count = int(count) - 1
		self.spinCountLabel.setText(new_count)

	def _zero_score(self):
		self.playerScore.setText("0")


# these functions do not have any subscriptions and thus need the data somehow.. therefore its not in the class?
#
def board_population(categories, round, self):
	# get all of the things the board needs to display immediately to the players.
	#

	# configure Jeopardy board.
	# assuming categories = ["elvis", "abbrev.", ...]
	#
	self.category1.setText(categories[0])
	self.category2.setText(categories[1])
	self.category3.setText(categories[2])
	self.category4.setText(categories[3])
	self.category5.setText(categories[4])
	self.category6.setText(categories[5])

	if round == 1:
		self.category1Cell1.setText(100)
		# do this for all category cells...? cant think of good for loop here..

	elif round == 2:
		self.category1Cell1.setText(200)

	else:
		print("invalid round value")
		exit(1)



def contestant_population(players, self):
	# configure today's contestants
	#
	self.player1Name.setText(players[0])
	self.player1Score.setText("0")
	self.player2Name.setText(players[1])
	self.player2Score.setText("0")
	self.player3Name.setText(players[2])
	self.player3Score.setText("0")




# MAIN PROGRAM
#
# define things to be used in the functions...
# players
# scores
# categories
# question_values

# call functions when things are heard from broadcasts
#



# Display GUI.
#
application = QApplication(sys.argv)
application.setApplicationName("Wheel of Jeopardy")
gui = ActivateWojApplication()
gui.show()
gui.raise_()
application.exec_()