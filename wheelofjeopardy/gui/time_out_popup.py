'''
This is a class called when the timer runs out.

@author = Miranda Link, mirandanlink@gmail.com
'''

from os import sys
from PyQt4.QtCore import Qt
from PyQt4.QtGui import *
from wheelofjeopardy.gui.pyqt.ui_time_out import Ui_TimeOutPopup
from wheelofjeopardy.events import Events

class TimeOutPopup(QDialog, Ui_TimeOutPopup):
    def __init__(self, events, answer, parent=None):
        super(TimeOutPopup, self).__init__(parent)

        # disable close/maximize/minimize buttons
        self.setWindowFlags(
            Qt.Dialog | Qt.WindowTitleHint | Qt.CustomizeWindowHint
        )

        self.setupUi(self)
        self.events = events

        # initialize variables
        #
        self.answerLabel.setText(answer)

#Display GUI.
if __name__ == '__main__':
    application = QApplication(sys.argv)
    application.setApplicationName("Time Out Popup")
    events = Events()
    gui = TimeOutPopup(events)
    gui.show()
    gui.raise_()
    application.exec_()
