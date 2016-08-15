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
    def __init__(self, events, game_state, parent=None):
        super(CategoryChoicePopup, self).__init__(parent)
        self.setupUi(self)
        self.events = events

        self.category_choice_buttons = [
            self.category1, self.category2, self.category3,
            self.category4, self.category5, self.category6
        ]

        self.category_choice_labels = [
            self.category1Label, self.category2Label, self.category3Label,
            self.category4Label, self.category5Label, self.category6Label
        ]

        current_round = game_state.current_round
        matrix = game_state.board._q_mat[current_round - 1]

        for idx in xrange(len(matrix.headers)):
            self.category_choice_labels[idx].setText(matrix.headers[idx])

            self.category_choice_buttons[idx].setEnabled(
                game_state.board.num_q_left_in_category(current_round, idx + 1) > 0
            )

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
