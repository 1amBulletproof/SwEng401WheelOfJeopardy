from os import sys
from PyQt4.QtGui import QMainWindow
from wheelofjeopardy.gui.pyqt.ui_category_choice_popup import Ui_CategoryChoicePopup

class CategoryChoicePopup(QMainWindow, Ui_CategoryChoicePopup):
  def __init__(self, parent=None):
    super(CategoryChoicePopup, self).__init__(parent)
    self.setupUi(self)
