'''
This is called to have a player accept or deny token use.

@author = Miranda Link, mirandanlink@gmail.com
'''

from os import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import pyqtSlot
from wheelofjeopardy.gui.pyqt.ui_token_popup import Ui_TokenPopup
from wheelofjeopardy.events import Events

class TokenPopup(QDialog, Ui_TokenPopup):
  def __init__(self, events, current_player, parent=None):
    super(TokenPopup, self).__init__(parent)
    self.setupUi(self)
    self.events = events

    # initialize variables
    #
    self.playerLabel.setText(current_player)

    # button clicks
    #
    @pyqtSlot()
    def _on_useTokenButton_clicked():
      self.events.broadcast('gui.use_free_token')

    @pyqtSlot()
    def _on_denyTokenButton_clicked():
      self.events.broadcast('gui.dont_use_free_token')


# Display GUI.
#
if __name__ == '__main__':
  application = QApplication(sys.argv)
  application.setApplicationName("Token Popup")
  events = Events()
  gui = TokenPopup(events)
  gui.show()
  gui.raise_()
  application.exec_()
