'''
This is a class that can be called to bring up the wojApplication gui.

@author = Miranda Link, mirandanlink@gmail.com
'''
# import pdb
import random
from os import sys
from PyQt4.QtGui import QMainWindow, QApplication
from PyQt4.QtCore import pyqtSlot

# this is the .py file spit out from PyQt
from wheelofjeopardy.gui.pyqt.ui_woj_application_window import Ui_WojApplicationWindow
from wheelofjeopardy.events import Events
from wheelofjeopardy.game_state import GameState
from wheelofjeopardy.player_state import PlayerState
from wheelofjeopardy.wheel import Wheel
from wheelofjeopardy.gui.moderator_popup import ModeratorPopup
from wheelofjeopardy.gui.category_choice_popup import CategoryChoicePopup
from wheelofjeopardy.gui.daily_double_popup import DailyDoublePopup
from wheelofjeopardy.gui.token_popup import TokenPopup
from wheelofjeopardy.utils.read_configs import read_cfg_to_options


class WojApplicationWindow(QMainWindow, Ui_WojApplicationWindow):
    def __init__(self, events, parent=None):
        super(WojApplicationWindow, self).__init__(parent)
        self.setupUi(self)
        self.events = events
        self.opts = read_cfg_to_options()

        self.category_labels = [
            self.category1, self.category2, self.category3,
            self.category4, self.category5, self.category6
        ]

        self.cell_matrix = [
            [self.category1Cell1, self.category1Cell2, self.category1Cell3, self.category1Cell4, self.category1Cell5],
            [self.category2Cell1, self.category2Cell2, self.category2Cell3, self.category2Cell4, self.category2Cell5],
            [self.category3Cell1, self.category3Cell2, self.category3Cell3, self.category3Cell4, self.category3Cell5],
            [self.category4Cell1, self.category4Cell2, self.category4Cell3, self.category4Cell4, self.category4Cell5],
            [self.category5Cell1, self.category5Cell2, self.category5Cell3, self.category5Cell4, self.category5Cell5],
            [self.category6Cell1, self.category6Cell2, self.category6Cell3, self.category6Cell4, self.category6Cell5]
        ]

        self.sector_category_map = [
            [1, 'category1'],  [2, 'category2'],       [3, 'category3'],
            [4, 'category4'],  [5, 'category5'],       [6, 'category6'],
            [7, 'Bankrupt'],   [8, 'FreeTurn'],        [9, 'LoseTurn'],
            [10, 'SpinAgain'], [11, 'OpponentChoice'], [12, 'PlayerChoice']
        ]

        self.players = [
            GuiPlayer(
                name_label=self.player1Name,
                score_label=self.player1Score,
                token_label=self.player1Tokens,
                player_state=PlayerState(
                    self.opts.player_names[0], self.events, self.opts.start_scores[0]
                )
            ),

            GuiPlayer(
                name_label=self.player2Name,
                score_label=self.player2Score,
                token_label=self.player2Tokens,
                player_state=PlayerState(
                    self.opts.player_names[1], self.events, self.opts.start_scores[1]
                )
            ),

            GuiPlayer(
                name_label=self.player3Name,
                score_label=self.player3Score,
                token_label=self.player3Tokens,
                player_state=PlayerState(
                    self.opts.player_names[2], self.events, self.opts.start_scores[2]
                )
            )
        ]

        # create the game state
        #
        self.game_state = GameState(
            [player.state for player in self.players], self.events, self.opts
        )

        # subscriptions
        #
        ## self.events.subscribe('board_sector.deactivate_square', self._deactivate_square)
        self.events.subscribe('player_choice_sector.choose_category', self._show_category_popup_player)
        self.events.subscribe('opponent_choice_sector.choose_category', self._show_category_popup_opponent)
        self.events.subscribe('board_sector.prompt_for_wager', self._show_daily_double_popup)
        ## self.events.subscribe('board_sector.received_invalid_wager', self._show_daily_double_popup)
        self.events.subscribe('player_state.spin_tokens_did_update', self._on_spin_tokens_did_update)
        self.events.subscribe('player_state.score_did_update', self._on_score_did_update)
        self.events.subscribe('sector.prompt_for_token_use', self._show_token_popup)
        ## self.events.subscribe('unknown', self._refire_token_popup) # not created yet
        ## self.events.subscribe('bankrupt_sector.update_score', self._zero_score) # do update score first
        ## self.events.subscribe('moderator.update_score', self._update_score) # do set player first
        self.events.subscribe('game_state.spins_did_update', self._on_spins_did_update)
        self.events.subscribe('game_state.game_did_end', self._game_end)
        self.events.subscribe('game_state.current_player_did_change', self._on_current_player_did_change)
        self.events.subscribe('board_sector.check_answer', self._on_check_answer)

        # put image behind wheel
        #

        # setup the player answer interface to not show "TextLabels" everywhere.
        #
        self.sectorOutput.setText("")
        self.currentQuestion.setText("")
        self.playerAnswerLabel.setText("")
        # self.spinCountValue.setText("50")

        # initialize variables - i.e. set up the entire board.
        #
        self.current_matrix = self.game_state.board._q_mat[0] # [0] means round 1, change later
        self.populate_board(self.current_matrix)

        for player in self.players:
            player.name_label.setText(player.state.name)

        # Let's go!
        self.events.broadcast('gui.game_will_start')

    # Methods that run on specific button clicks
    #
    @pyqtSlot()
    def on_spinButton_clicked(self):
        # broadcast that the spin button was clicked
        #
        print("spinning...")
        self.game_state.spin() #quick fix, need to use broadcast
        #self.events.broadcast('gui.spin_happened')

        # animate the wheel
        #

        # get category landed on
        #
        current_sector = self.game_state.current_sector
        ## for sector in self.sectorCategoryMap:
        ##     print(current_sector, sector)
        ##     if str(current_sector) in sector[1]:
        ##         current_sector_number = sector[0]
        #current_sector_numbers = self.wheel._initialize_sectors
        #print(current_sector_numbers)

        # put wheel at location
        #
        #self.dial.setValue(current_sector_number)

        # populate current category for answer area
        #
        current_category = self.game_state.current_category
        if type(current_category) is int:
            headers_index = current_category - 1
            current_category_text = self.current_matrix.headers[headers_index]
            self.sectorOutput.setText(current_category_text)

            # populate current question to be answered
            #
            question = self.game_state.next_question_in_category(current_category)
            question = str(question).split(":")[0]
            if question != "None":
                self.currentQuestion.setText(question)
            else:
                pass
                #self.currentQuestion.setText(current_category)
        else:
            self.sectorOutput.setText("not a category!")

    @pyqtSlot() #WAHOO
    def on_submitAnswerButton_clicked(self):
        player_answer = self.playerAnswerEntryBox.toPlainText()
        print("submitting...")
        self.events.broadcast('gui.answer_received', player_answer)

    # Functions that run from subscriptions
    #
    def _on_check_answer(self, question, player_answer): #WAHOO
        # call moderator popup
        #
        print("checking...")

        dialog = ModeratorPopup(
            events=self.events, question=question, player_answer=player_answer,
            parent=self
        )

        dialog.exec_()

    def _on_score_did_update(self, player_state):
        player = self._find_player(player_state)
        player.score_label.setText(str(player_state.score))

    def _on_spin_tokens_did_update(self, player_state):
        player = self._find_player(player_state)
        player.token_label.setText(str(player_state.free_spin_tokens))

    def _find_player_index(self, player_state):
        for idx, player in enumerate(self.players):
            if player.state == player_state:
                return idx

        return None

    def _find_player(self, player_state):
        idx = self._find_player_index(player_state)
        return self.players[idx]

    def _deactivate_square(self, square): # no broadcast for this
        # when a square's question has been shown to the user
        #
        self.square.setEnabled(False)


    def _game_end(self):
        # deactivate buttons
        #
        self.spinButton.setEnabled(False)
        self.submitAnswerButton.setEnabled(False)


    def _on_current_player_did_change(self, game_state): #WAHOO
        # set the current player for the answer area
        #
        player = self.game_state.get_current_player()
        cur_idx = self._find_player_index(player)
        cur_gui_player = self.players[cur_idx]

        self.playerAnswerLabel.setText(player.name)
        self._set_bold(cur_gui_player.name_label, True)

        for idx, gui_player in enumerate(self.players):
            if idx != cur_idx:
                self._set_bold(gui_player.name_label, False)

    def _set_bold(self, label, bold=True):
        font = label.font()
        font.setBold(bold)
        label.setFont(font)

    def _show_category_popup_player(self, jeopardy_board): # not communicating choice correctly
        # call category_choice_popup for the current player
        #
        self.dialog = CategoryChoicePopup(events=self.events, categories=self.jeopardy_board.headers, parent=self)
        self.dialog.titleLabel.setText("current player, choose a category!")
        self.dialog.exec_()

    def _show_category_popup_opponent(self, jeopardy_board): # not communicating choice correctly
        # call category_choice_popup for the opponents
        #
        self.dialog = CategoryChoicePopup(events=self.events, categories=self.jeopardy_board.headers, parent=self)
        self.dialog.titleLabel.setText("opponents, collaborate and choose a category!")
        self.dialog.exec_()


    def _show_daily_double_popup(self, min_wager, max_wager): #WAHOO
        # call daily_double_popup
        #
        self.dialog = DailyDoublePopup(events=self.events, min_wager=min_wager, max_wager=max_wager, parent=self)
        self.dialog.exec_()


    def _show_token_popup(self): #WAHOO
        # call token_popup
        current_player = self.game_state.get_current_player().name
        self.dialog = TokenPopup(events=self.events, current_player=current_player, parent=self)
        self.dialog.exec_()


    def _on_spins_did_update(self, game_state): #WAHOO
        if self.game_state.spins_remaining <= 0:
            self.spinButton.setEnabled(False)

        self.spinCountValue.setText(str(self.game_state.spins_remaining))


    # functions that are just being functions
    #
    def populate_board(self, question_matrix):
        # configure Jeopardy board.
        #
        for category_index in xrange(len(question_matrix.headers)):
            self.category_labels[category_index].setText(question_matrix.headers[category_index])

        for category_row in xrange(len(self.cell_matrix)):
            for category_column in xrange(len(self.cell_matrix[category_row])):
                self.cell_matrix[category_row][category_column].setText(
                    str(question_matrix.pointValues[category_column])
                )

class GuiPlayer(object):
    def __init__(self, player_state, name_label, score_label, token_label):
        self.state = player_state
        self.name_label = name_label
        self.score_label = score_label
        self.token_label = token_label

# MAIN PROGRAM
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
