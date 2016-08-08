'''
This class is called to show categories to the user.

@author = Miranda Link, mirandanlink@gmail.com
'''

from os import sys
from PyQt4.QtGui import *
from wheelofjeopardy.gui.pyqt.ui_category_choice_popup import Ui_CategoryChoicePopup
from wheelofjeopardy.events import Events

class CategoryChoicePopup(QDialog, Ui_CategoryChoicePopup):
  def __init__(self, events, parent=None):
    super(CategoryChoicePopup, self).__init__(parent)
    self.setupUi(self)
    self.events = events

    # initialize variables
    #

    # disable categories if applicable
    #

    # button clicks
    #
    def _on_category1_clicked(self):
      self.events.broadcast('gui.category_chosen', 1)

    def _on_category2_clicked(self):
      self.events.broadcast('gui.category_chosen', 2)

    def _on_category3_clicked(self):
      self.events.broadcast('gui.category_chosen', 3)

    def _on_category4_clicked(self):
      self.events.broadcast('gui.category_chosen', 4)

    def _on_category5_clicked(self):
      self.events.broadcast('gui.category_chosen', 5)

    def _on_category6_clicked(self):
      self.events.broadcast('gui.category_chosen', 6)
    


#Display GUI.
if __name__ == '__main__':
  application = QApplication(sys.argv)
  application.setApplicationName("Category Choice Popup")
  events = Events()
  gui = CategoryChoicePopup(events)
  gui.show()
  gui.raise_()
  application.exec_()

# subscriptions
#
events.subscribe('gui.show_token_popup', CategoryChoicePopup)
