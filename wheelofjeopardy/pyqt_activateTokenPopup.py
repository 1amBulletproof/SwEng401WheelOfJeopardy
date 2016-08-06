'''
This class brings up the token popup when WojApplication runs show_token_popup()

@author = Miranda Link, mirandanlink@gmail.com
'''

import TokenDialog

class ActivateTokenPopup(QDialog, TokenDialog.Ui_TokenDialog):
	def __init__(self, parent=WojApplication):
		self.setupUi(self)

		# initialize variables
		#
		self.playerLabel.setText(current_player)

	# button clicks
	#
	@pyqtSignature("")
	def on_useTokenButton_clicked(self):
		self.broadcast('gui.use_free_token')

	@pyqtSignature("")
	def on_denyTokenButton_clicked(self):
		self.broadcast('gui.dont_use_free_token')