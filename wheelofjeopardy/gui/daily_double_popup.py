from os import sys
from PyQt4.QtGui import QMainWindow
from wheelofjeopardy.gui.pyqt.ui_daily_double_popup import Ui_DailyDoublePopup

class DailyDoublePopup(QMainWindow, Ui_DailyDoublePopup):
  def __init__(self, parent=None):
    super(DailyDoublePopup, self).__init__(parent)
    self.setupUi(self)
