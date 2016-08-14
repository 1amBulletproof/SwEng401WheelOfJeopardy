'''
This is a class that can be called to bring up the wojApplication gui.

@author = Miranda Link, mirandanlink@gmail.com
'''
# import pdb
import random
import time
from os import sys

from PyQt4.QtGui import QMainWindow, QApplication, QPixmap
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
from wheelofjeopardy.gui.wheel_view import WheelView
from wheelofjeopardy.gui.round_game_popup import RoundGamePopup
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
            [self.category1Cell1, self.category2Cell1, self.category3Cell1, self.category4Cell1, self.category5Cell1, self.category6Cell1],
            [self.category1Cell2, self.category2Cell2, self.category3Cell2, self.category4Cell2, self.category5Cell2, self.category6Cell2],
            [self.category1Cell3, self.category2Cell3, self.category3Cell3, self.category4Cell3, self.category5Cell3, self.category6Cell3],
            [self.category1Cell4, self.category2Cell4, self.category3Cell4, self.category4Cell4, self.category5Cell4, self.category6Cell4],
            [self.category1Cell5, self.category2Cell5, self.category3Cell5, self.category4Cell5, self.category5Cell5, self.category6Cell5],
        ]

        self.sector_category_map = [
            [1, 'category1'],  [2, 'category2'],       [3, 'category3'],
            [4, 'category4'],  [5, 'category5'],       [6, 'category6'],
            [7, 'Bankrupt'],   [8, 'FreeSpin'],        [9, 'LoseTurn'],
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
        ## self.events.subscribe('player_state.deactivate_square', self._deactivate_square) # animation
        self.events.subscribe('player_choice_sector.choose_category', self._show_category_popup_player)
        self.events.subscribe('opponent_choice_sector.choose_category', self._show_category_popup_opponent)
        self.events.subscribe('board_sector.prompt_for_wager', self._show_daily_double_popup)
        self.events.subscribe('board_sector.question_will_be_asked', self._on_question_will_be_asked)
        ## self.events.subscribe('board_sector.received_invalid_wager', self._show_daily_double_popup)
        self.events.subscribe('player_state.spin_tokens_did_update', self._on_spin_tokens_did_update)
        self.events.subscribe('player_state.score_did_update', self._on_score_did_update)
        self.events.subscribe('player_state.score_did_update', self._clear_answer_area)
        self.events.subscribe('sector.prompt_for_token_use', self._show_token_popup)
        self.events.subscribe('sector.no_questions_in_category', self._no_questions_left)
        ## self.events.subscribe('unknown', self._refire_token_popup) # not created yet
        ## self.events.subscribe('bankrupt_sector.update_score', self._zero_score) # do update score first
        self.events.subscribe('game_state.spins_did_update', self._on_spins_did_update)
        self.events.subscribe('game_state.announce_winners', self._game_end)
        self.events.subscribe('game_state.round_did_end', self._round_end)
        self.events.subscribe('game_state.current_player_did_change', self._on_current_player_did_change)
        self.events.subscribe('game_state.sector_was_chosen', self._on_sector_was_chosen)
        self.events.subscribe('board_sector.check_answer', self._on_check_answer)

        self.events.subscribe('question_timer.tick', self._on_question_timer_tick)
        self.events.subscribe('question_timer.has_expired', self._on_question_timer_has_expired)

        # put image behind wheel
        #

        # setup the player answer interface to not show "TextLabels" everywhere.
        #
        self.sectorOutput.setText("")
        self.currentQuestion.setText("")
        self.playerAnswerLabel.setText("")
        self.timeRemainingValue.setText("")
        self.indicatorLabel.setPixmap(QPixmap('wheelofjeopardy/indicator.png'))

        self.wheel_view = WheelView(self.wheelView)
        self.wheel_view.on_finished = self._on_wheel_spin_finished

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
        self._update_question_board()
        self.events.broadcast('gui.spin')
        self.sectorOutput.setText("None")

    @pyqtSlot() #WAHOO
    def on_submitAnswerButton_clicked(self):
        player_answer = self.playerAnswerEntryBox.toPlainText()
        print("submitting...")
        self.events.broadcast('gui.answer_received', player_answer)

    # Functions that run from subscriptions
    #
    def _clear_answer_area(self, *args):
        self.sectorOutput.setText("")
        self.currentQuestion.setText("")
        self.playerAnswerEntryBox.setText("")

    def _deactivate_square(self, square):
        # when a square's question has been shown to the user
        #
        self.square.setEnabled(False)

    def _on_sector_was_chosen(self, sector):
        self.wheel_view.spin_to_sector(sector.name)

    def _on_wheel_spin_finished(self):
        self.currentQuestion.setText("you landed on {}!".format(self.game_state.current_sector.name))
        self.events.broadcast(
            'gui.trigger_sector_action', self.game_state.current_sector
        )

    def _on_question_will_be_asked(self, question):
        self.sectorOutput.setText(question.category_header)
        self.currentQuestion.setText(question.text)
        self._update_question_board()

    def _update_question_board(self):
        status_matrix = self.game_state.board._get_board_q_status()
        current_question = self.game_state.current_question

        if current_question != None:
            print 'row %d col %d' % (current_question.row, current_question.column)

        for row_idx, row in enumerate(status_matrix):
            for col_idx, visible in enumerate(row):
                cell = self.cell_matrix[row_idx][col_idx]

                cell_is_current = current_question != None and \
                    col_idx == current_question.column and \
                    row_idx == current_question.row

                if cell_is_current:
                    cell.setStyleSheet('background-color: blue; color: white')
                    cell.setVisible(True)
                else:
                    cell.setStyleSheet('background-color: none; color: black')
                    cell.setVisible(visible)

    def _on_question_timer_tick(self, remaining):
        self.timeRemainingValue.setText(str(remaining))

    def _on_question_timer_has_expired(self):
        print 'Expired!'

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
        # call clear answer area and deactivate square
        #
        #square =
        self._clear_answer_area()
        #self._deactivate_square(self, square)

    def _on_spin_tokens_did_update(self, player_state):
        player = self._find_player(player_state)
        print(player.state.free_spin_tokens)
        player.token_label.setText(str(player.state.free_spin_tokens))


    def _find_player_index(self, player_state):
        for idx, player in enumerate(self.players):
            if player.state == player_state:
                return idx
        return None


    def _find_player(self, player_state):
        idx = self._find_player_index(player_state)
        return self.players[idx]


    def _game_end(self, winner):
        # show winner
        #
        dialog = RoundGamePopup(
            events=self.events, round=False, winner=winner,
            parent=self
        )
        dialog.exec_()

    def _no_questions_left(self, category):
        self.currentQuestion.setText("no questions left in %s. spin again!" % category.name)

    def _round_end(self, game_state):
        # start round 2 population
        #
        self.current_matrix = self.game_state.board._q_mat[1] # [0] means round 1
        self.populate_board(self.current_matrix)

        dialog = RoundGamePopup(
            events=self.events, round=True, winner=None,
            parent=self
        )
        dialog.exec_()

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

    def _show_category_popup_player(self, current_matrix): #WAHOO
        # call category_choice_popup for the current player
        #
        self.dialog = CategoryChoicePopup(events=self.events, categories=self.current_matrix.headers, parent=self)
        self.dialog.titleLabel.setText("current player, choose a category!")
        self.dialog.exec_()

    def _show_category_popup_opponent(self, current_matrix): #WAHOO
        # call category_choice_popup for the opponents
        #
        self.dialog = CategoryChoicePopup(events=self.events, categories=self.current_matrix.headers, parent=self)
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
                    str(question_matrix.pointValues[category_row])
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
