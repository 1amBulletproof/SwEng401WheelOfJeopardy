'''
This is a class called when "submit answer" button is clicked.

@author = Miranda Link, mirandanlink@gmail.com
'''

from os import sys
from PyQt4.QtCore import pyqtSlot
from PyQt4.QtGui import *
from wheelofjeopardy.gui.pyqt.ui_moderator_popup import Ui_ModeratorPopup
from wheelofjeopardy.events import Events


class ModeratorPopup(QDialog, Ui_ModeratorPopup):
  def __init__(self, events, question, player_answer, parent=None):
    super(ModeratorPopup, self).__init__(parent)
    self.setupUi(self)

    self.events = events
    self.question = question
    self.player_answer = player_answer

    # initialize variables
    #
    self.correctAnswer.setText(question.answer)
    self.playerAnswer.setText(player_answer)

  # button clicks
  #
  @pyqtSlot()
  def on_okButton_clicked(self):
    if self.playerCorrectRadio.isChecked():
      self.events.broadcast('gui.correct_answer_received', self.question)
    else:
      self.events.broadcast('gui.incorrect_answer_received', self.question)


#Display GUI.
if __name__ == '__main__':
  application = QApplication(sys.argv)
  application.setApplicationName("Moderator Popup")
  events = Events()
  gui = ModeratorPopup(events)
  gui.show()
  gui.raise_()
  application.exec_()

