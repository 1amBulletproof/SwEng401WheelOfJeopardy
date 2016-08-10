'''
This is a clas that can be called when a daily double square has been landed on

@author = Miranda Link, mirandanlink@gmail.com
'''

from os import sys
from PyQt4.QtGui import *
from wheelofjeopardy.gui.pyqt.ui_daily_double_popup import Ui_DailyDoublePopup
from wheelofjeopardy.events import Events

class DailyDoublePopup(QDialog, Ui_DailyDoublePopup):
  def __init__(self, events, parent=None):
    super(DailyDoublePopup, self).__init__(parent)
    self.setupUi(self)
    self.events = events

    # button clicks
    #
    def _on_submitWagerButton_clicked():
      wager = self.wagerAmount.text()
      self.events.broadcast('gui.wager_received')


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


