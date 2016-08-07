from os import sys
from PyQt4.QtGui import QMainWindow
from wheelofjeopardy.gui.pyqt.ui_moderator_popup import Ui_ModeratorPopup

class ModeratorPopup(QMainWindow, Ui_ModeratorPopup):
  def __init__(self, parent=None):
    super(ModeratorPopup, self).__init__(parent)
    self.setupUi(self)
