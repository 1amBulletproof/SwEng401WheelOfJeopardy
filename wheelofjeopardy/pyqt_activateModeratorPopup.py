'''
This class brings up the moderator popup when WojApplication runs show_moderator_popup()

@author = Miranda Link, mirandanlink@gmail.com
'''

import ModeratorDialog

class ActivateModeratorPopup(QDialog, ModeratorDialog.Ui_ModeratorDialog):
	def __init__(self, parent=None):
		super(ActivateModeratorPopup, self).__init__(parent)
		self.setupUi(self)

		# initialize variables
		#
		self.correctAnswer.setText(correct_answer)
		self.playerAnswer.setText(player_answer)


	# button clicks
	#
	@pyqtSignature("")
	def on_playerCorrectRadio_clicked(self):
		self.broadcast('gui.correct_answer_received')
		self.broadcast('moderator.update_score')

	@pyqtSignature("")
	def on_playerIncorrectRadio_clicked(self):
		self.broadcast('gui.incorrect_answer_received')