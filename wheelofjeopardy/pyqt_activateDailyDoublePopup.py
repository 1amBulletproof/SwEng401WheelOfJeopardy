'''
This class brings up the daily double popup when WojApplication runs show_daily_double_popup()

@author = Miranda Link, mirandanlink@gmail.com
'''

import dailyDoubleDialog

class ActivateDailyDoublePopup(QDialog, DailyDoubleDialog.Ui_DailyDoubleDialog):
	def __init__(self, parent=None):
		super(ActivateDailyDoublePopup, self).__init__(parent)
		self.setupUi(self)

	# button click
	#
	@pyqtSignature("")
	def on_submitWagerButton_clicked(self):
		wager = self.wagerAmount.text()
		wager = int(wager)
		self.broadcast('gui.wager_received', wager)
