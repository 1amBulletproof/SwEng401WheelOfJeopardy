'''
This class is called to show categories to the user.

@author = Miranda Link, mirandanlink@gmail.com
'''

from os import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import pyqtSlot
from wheelofjeopardy.gui.pyqt.ui_category_choice_popup import Ui_CategoryChoicePopup
from wheelofjeopardy.events import Events

class CategoryChoicePopup(QDialog, Ui_CategoryChoicePopup):
    def __init__(self, events, categories, parent=None):
        super(CategoryChoicePopup, self).__init__(parent)
        self.setupUi(self)
        self.events = events
        self.categoryChoiceLabels = [
            self.category1Label, self.category2Label, self.category3Label,
            self.category4Label, self.category5Label, self.category6Label
        ]

        # initialize variables
        #
        for categoryIndex in xrange(len(categories)):
            self.categoryChoiceLabels[categoryIndex].setText(categories[categoryIndex])

    # disable categories if applicable
    #

    # button clicks
    #
    @pyqtSlot()
    def on_category1_clicked(self):
        self.events.broadcast('gui.category_chosen', 1)

    @pyqtSlot()
    def on_category2_clicked(self):
        self.events.broadcast('gui.category_chosen', 2)

    @pyqtSlot()
    def on_category3_clicked(self):
        self.events.broadcast('gui.category_chosen', 3)

    @pyqtSlot()
    def on_category4_clicked(self):
        self.events.broadcast('gui.category_chosen', 4)

    @pyqtSlot()
    def on_category5_clicked(self):
        self.events.broadcast('gui.category_chosen', 5)

    @pyqtSlot()
    def on_category6_clicked(self):
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
