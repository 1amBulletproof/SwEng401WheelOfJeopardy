from os import sys
from PyQt4.QtGui import QMainWindow
from wheelofjeopardy.gui.pyqt.ui_token_popup import Ui_TokenPopup

class TokenPopup(QMainWindow, Ui_TokenPopup):
  def __init__(self, parent=None):
    super(TokenPopup, self).__init__(parent)
    self.setupUi(self)
