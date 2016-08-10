'''
This is a class that can be called to bring up the wojApplication gui.

@author = Miranda Link, mirandanlink@gmail.com
'''
#import pdb
from os import sys
from PyQt4.QtGui import QMainWindow, QApplication
from PyQt4.QtCore import pyqtSignature

# this is the .py file spit out from PyQt
#from wheelofjeopardy.gui.moderator_popup import ModeratorPopup
from wheelofjeopardy.gui.pyqt.ui_woj_application_window import Ui_WojApplicationWindow
from wheelofjeopardy.events import Events
from wheelofjeopardy.game_state import GameState
from wheelofjeopardy.player_state import PlayerState
from wheelofjeopardy.gui.moderator_popup import ModeratorPopup
from wheelofjeopardy.utils.read_configs import ReadCfgToOptions

class WojApplicationWindow(QMainWindow, Ui_WojApplicationWindow):
    def __init__(self, events, parent=None):
        super(WojApplicationWindow, self).__init__(parent)
        self.setupUi(self)
        self.events = events
        self.opts = ReadCfgToOptions()
        self.categoryLabels = [self.category1, self.category2, self.category3,
                               self.category4, self.category5, self.category6]
        self.cellMatrix = [[self.category1Cell1, self.category1Cell2, self.category1Cell3, self.category1Cell4, self.category1Cell5],
                           [self.category2Cell1, self.category2Cell2, self.category2Cell3, self.category2Cell4, self.category2Cell5],
                           [self.category3Cell1, self.category3Cell2, self.category3Cell3, self.category3Cell4, self.category3Cell5],
                           [self.category4Cell1, self.category4Cell2, self.category4Cell3, self.category4Cell4, self.category4Cell5],
                           [self.category5Cell1, self.category5Cell2, self.category5Cell3, self.category5Cell4, self.category5Cell5],
                           [self.category6Cell1, self.category6Cell2, self.category6Cell3, self.category6Cell4, self.category6Cell5]]


        # subscriptions
        #
        ## self.events.subscribe('board_sector.deactivate_square', self._deactivate_square)
        ## self.events.subscribe('player_choice_sector.choose_category', self._show_category_popup)
        ## self.events.subscribe('opponent_choice_sector.choose_category', self._show_category_popup)
        ## self.events.subscribe('board_sector.prompt_for_wager', self._show_daily_double_popup)
        ## self.events.subscribe('sector.prompt_for_token_use', self._show_token_popup)
        ## self.events.subscribe('bankrupt_sector.update_score', self._zero_score)
        ## self.events.subscribe('moderator.update_score', self._update_score)
        ## self.events.subscribe('game_state.spins_did_update', self._update_spin_count)
        ## self.events.subscribe('game_state.game_did_end', self._game_end)
        ## self.events.subscribe('player_state.current_player_did_change', self._set_player)
        self.events.subscribe('board_sector.check_answer', self._on_check_answer)

        # put image behind wheel
        #

        # click stuff
        #
        self.submitAnswerButton.clicked.connect(self.on_submitAnswerButton_clicked)
        self.spinButton.clicked.connect(self.on_spinButton_clicked)
        
        # setup the player answer interface to not show "TextLabels" everywhere.
        #
        self.sectorOutput.setText("")
        self.currentQuestion.setText("")
        self.playerAnswerLabel.setText("")
        self.spinCountValue.setText("50")

        # create the game state
        #
        players = [PlayerState(self.opts.playerNames[n], self.events, self.opts.startScores[n])
                   for n in range(self.opts.nPlayers)]
        self.game_state = GameState(players, self.events, self.opts)


        # initialize variables - i.e. set up the entire board.
        #
        self.board_population(self.game_state.board._q_mat[0]) # [0] means round 1, change later
        # self.contestant_population(player_state.players, self)


    # Methods that run on specific button clicks
    #
    @pyqtSignature("")
    def on_spinButton_clicked(self):
        # broadcast that the spin button was clicked
        #
        print("spinning...")
        self.game_state.spin()
        #self.events.broadcast('gui.spin_happened')
        # animate the wheel
        #


    @pyqtSignature("") #WAHOO
    def on_submitAnswerButton_clicked(self):
        # call moderator_popup
        #
        player_answer = self.playerAnswerEntryBox.toPlainText()
        print("submitting...")
        self.events.broadcast('gui.answer_received', player_answer)
        
    # Functions that run from subscriptions
    #
    def _on_check_answer(self, question, player_answer): #WAHOO
        print("checking...")
        self.dialog = ModeratorPopup(events=self.events, correct_answer=question.answer,
                                     player_answer=player_answer, parent=self)
        self.dialog.exec_()

    def _deactivate_square(self, square):
        # when a square's question has been shown to the user
        #
        self.square.setEnabled(False)


    def _game_end(self):
        pass


    def _set_player(self):
        # set the current player for the answer area
        #
        self.playerAnswerLabel.setText(current_player)

        # bold the current player in the player area
        #
        self.playerName.setFont.setBold(True)
        pass

    def _show_category_popup(self):
        # call category_choice_popup
        #
        pass


    def _show_daily_double_popup(self):
        # call daily_double_popup
        self.events.broadcast('gui.show_dailydouble_popup')
    

    def _show_token_popup(self):
        # call token_popup
        self.events.broadcast('gui.show_token_popup')
        
    def _update_score(self):
        # needs to know current player..
        #
        current_score = self.playerScore.text()
        new_score = int(current_score) + question_point_value
        self.playerScore.setText(new_score)
        pass

    def _update_spin_count(self):
        count = self.spinCountLabel.text()
        new_count = int(count) - 1
        self.spinCountLabel.setText(new_count)

    def _zero_score(self):
        self.playerScore.setText("0")


    # functions that are just being functions
    # 
    def board_population(self, question_matrix):
        # configure Jeopardy board.
        #
        for categoryIndex in xrange(len(question_matrix.headers)):
            self.categoryLabels[categoryIndex].setText(question_matrix.headers[categoryIndex])

        for categoryRow in xrange(len(self.cellMatrix)):
            for categoryColumn in xrange(len(self.cellMatrix[categoryRow])):
                self.cellMatrix[categoryRow][categoryColumn].setText(str(question_matrix.pointValues[categoryColumn]))
            

def contestant_population(players, self):
    # configure today's contestants
    #
    self.player1Name.setText(players[0])
    self.player1Score.setText("0")
    self.player2Name.setText(players[1])
    self.player2Score.setText("0")
    self.player3Name.setText(players[2])
    self.player3Score.setText("0")




# MAIN PROGRAM
#
# define things to be used in the functions...
# players
# scores
# categories
# question_values

# call functions when things are heard from broadcasts
#



# Display GUI.
#

if __name__ == '__main__':
    application = QApplication(sys.argv)
    application.setApplicationName("Wheel of Jeopardy")
    events = Events()
    gui = WojApplicationWindow(events)
    gui.show()
    gui.raise_()
    application.exec_()
