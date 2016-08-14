'''
This is a class that can be called when a daily double square has been landed on

@author = Miranda Link, mirandanlink@gmail.com
'''

from os import sys
from PyQt4.QtGui import *
from wheelofjeopardy.gui.pyqt.ui_daily_double_popup import Ui_DailyDoublePopup
from wheelofjeopardy.events import Events

class DailyDoublePopup(QDialog, Ui_DailyDoublePopup):
    def __init__(self, min_wager, max_wager, parent=None):
        super(DailyDoublePopup, self).__init__(parent)
        self.setupUi(self)

        # initialize variables
        #
        min_wager = str(min_wager)
        max_wager = str(max_wager)

        self.maxLabelValue.setText(max_wager)
        self.minLabelValue.setText(min_wager)

    # button clicks
    #
    def on_submitWagerButton_clicked(self):
        self.wager = int(self.wagerAmount.text())

# Display GUI.
#
if __name__ == '__main__':
    application = QApplication(sys.argv)
    application.setApplicationName("Daily Double Popup")
    events = Events()
    gui = DailyDoublePopup(events)
    gui.show()
    gui.raise_()
    application.exec_()
