'''
This is a class called when a round or the game is over.

@author = Miranda Link, mirandanlink@gmail.com
'''

from os import sys
from PyQt4.QtCore import pyqtSlot
from PyQt4.QtGui import *
from wheelofjeopardy.gui.pyqt.ui_round_game_over import Ui_RoundGamePopup
from wheelofjeopardy.events import Events


class RoundGamePopup(QDialog, Ui_RoundGamePopup):
    def __init__(self, events, round=False, winner=None, parent=None):
        super(RoundGamePopup, self).__init__(parent)
        self.setupUi(self)

        self.events = events

        # initialize variables
        #
        if round:
            self.roundOrGameLabel.setText("Round 1")
            self.winnerLabel.setText("")
        else:
            self.roundOrGameLabel.setText("The Game")
            self.winnerLabel.setText("{} is the winner!".format(winner[0]))

# Display GUI.
if __name__ == '__main__':
    application = QApplication(sys.argv)
    application.setApplicationName("Round or Game Popup")
    events = Events()
    gui = RoundGamePopup(events)
    gui.show()
    gui.raise_()
    application.exec_()
