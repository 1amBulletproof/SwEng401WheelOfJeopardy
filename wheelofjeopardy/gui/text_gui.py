import sys
import os

from wheelofjeopardy.events import Events
from wheelofjeopardy.player_state import PlayerState
from wheelofjeopardy.game_state import GameState
from wheelofjeopardy.text_helper import apostrophize, pluralize
from wheelofjeopardy.utils.read_configs import read_cfg_to_options

class TextGUI(object):
    @classmethod
    def start(cls):
        print 'Welcome to Wheel of Jeopardy!'
        print "Let's get started!"
        global opts

        events = Events()
        opts = read_cfg_to_options()
        TextGUI(cls._create_game_state(events), events)._start()

    # private static

    @classmethod
    def _create_game_state(cls, events):
        players = [
            PlayerState(opts.player_names[n], events, opts.start_scores[n])
                for n in range(opts.n_players)
        ]

        return GameState(players, events, opts)

    @staticmethod
    def _clear_terminal():
        raw_input('Press Enter to continue...')
        os.system('cls' if os.name == 'nt' else 'clear')

    # public instance

    def __init__(self, game_state, events):
        self.game_state = game_state
        self.events = events

    # private instance

    def _start(self):
        self.events.subscribe('game_state.current_player_did_change', self._on_current_player_did_change)
        self.events.subscribe('game_state.spins_did_update', self._on_spins_did_update)
        self.events.subscribe('game_state.turn_will_end', self._on_turn_will_end)
        self.events.subscribe('game_state.sector_was_chosen', self._on_sector_was_chosen)
        self.events.subscribe('game_state.round_did_end', self._on_round_did_end)
        self.events.subscribe('game_state.game_did_end', self._on_game_did_end)
        self.events.subscribe('game_state.announce_winners', self._on_announce_winners)

        self.events.subscribe('opponent_choice_sector.choose_category', self._on_prompt_for_category)
        self.events.subscribe('player_choice_sector.choose_category', self._on_prompt_for_category)

        self.events.subscribe('board_sector.question_will_be_asked', self._on_question_will_be_asked)
        self.events.subscribe('board_sector.daily_double_selected', self._on_daily_double_selected)
        self.events.subscribe('board_sector.check_answer', self._on_check_answer)
        self.events.subscribe('sector.prompt_for_token_use', self._on_prompt_for_token_use)
        self.events.subscribe('sector.no_questions_in_category', self._on_no_questions_in_category)
        self.events.subscribe('board_sector.prompt_for_wager', self._on_prompt_for_wager)
        self.events.subscribe('board_sector.received_invalid_wager', self._on_received_invalid_wager)

        TextGUI._clear_terminal()

        self.events.broadcast('gui.game_will_start')

        while not self.game_state.has_game_ended():
            print(self.game_state.board)
            print 'What would you like to do, %s?' % \
                self.game_state.get_current_player().name
            sys.stdout.write("(S)pin, (Q)uit, (P)rint scores: ")
            answer = raw_input().lower()

            if answer == 's':
                self.events.broadcast('gui.spin')
            elif answer == 'p':
                self._print_scores()
            elif answer == 'q':
                break
            elif len(answer)>0 and answer[0] == 'c': # cheat menu
                self.game_state._cheat(answer[1:])

        print 'Good game!'

    def _on_current_player_did_change(self, game_state):
        print self._get_whose_turn_message()

    def _on_spins_did_update(self, game_state):
        print self._get_spins_remaining_message()
        TextGUI._clear_terminal()

    def _on_sector_was_chosen(self, sector):
        print('You spun %s.' % str(sector))

    def _on_turn_will_end(self, game_state):
        print 'That concludes %s turn.' % apostrophize(game_state.get_current_player().name)

    def _on_question_will_be_asked(self, question):
        print "Alright, here's the %d-point question in %s:" % (
            question.point_value, question.category_header
        )

        sys.stdout.write('%s: ' % (question.text))
        answer = raw_input()
        self.events.broadcast('gui.answer_received', answer)

    def _on_check_answer(self, question, answer):
        player_name = self.game_state.get_current_player().name
        print 'Correct answer is: %s' % (question.answer)
        prompt = 'Hey moderator, is %s answer correct (y/n)? ' % (apostrophize(player_name))

        if self._prompt_yes_no(prompt):
            self.events.broadcast('gui.correct_answer_received', question)
        else:
            self.events.broadcast('gui.incorrect_answer_received', question)

    def _on_prompt_for_category(self, person='Please'):
        '''
        Optional parameter person contains the text that would be displayed
        on the prompt.
        '''
        sys.stdout.write("%s, enter a number 1-6 for the category "%person +\
                         "you wish to choose: ")
        answer = raw_input()
        print 'You answered: %s' %(answer)
        while (not answer.isdigit()) or (int(answer) > 6 or int(answer) < 0):
            sys.stdout.write("Incorrect format. Please enter a number 1-6: ")
            answer = raw_input()
        #game_state is listening
        self.events.broadcast('gui.category_chosen', int(answer))

    def _on_prompt_for_token_use(self):
        prompt = 'Would you like to use one of your free spin tokens (y/n)? '

        if self._prompt_yes_no(prompt):
            self.events.broadcast('gui.use_free_token')
        else:
            self.events.broadcast('gui.dont_use_free_token')

    def _on_no_questions_in_category(self, category):
        print 'No questions remaining in category %s, spin again.' % (category)

    def _on_daily_double_selected(self):
        print 'DAILY DOUBLE!!'

    def _on_prompt_for_wager(self, min_wager, max_wager):
        self._print_scores(clear=False)
        print "You can wager between %d and %d points." % (min_wager, max_wager)
        wager = self._prompt_number("What's your wager? ")
        self.events.broadcast('gui.wager_received', wager)

    def _on_received_invalid_wager(self):
        print "Sorry, that's an invalid wager amount. Try again."

    def _on_round_did_end(self, game_state):
        print('That concludes round %u.' % game_state.current_round)
        self._print_scores() # print end-of-round scores

    def _on_game_did_end(self, game_state):
        print('Game over!')
        self._print_scores() # print end-of-game scores

    def _on_announce_winners(self, winners):
        self._print_winners(winners)

    def _print_scores(self, clear=True):
        score_strings = []

        for pl in self.game_state.player_states:
            score_strings.append("\t%s has %u points, %u tokens." % \
                                 (pl.name, pl.score, pl.free_spin_tokens) )

        print 'Here are the scores:'
        print '\n'.join(score_strings)

        if clear:
            TextGUI._clear_terminal()

    def _print_winners(self, winners):
        outStr = 'The winner(s):\n'
        for p in winners:
            outStr += '\t%s\n'%p
        print(outStr)

    def _get_spins_remaining_message(self):
        spins = self.game_state.spins_remaining

        return "There %s remaining." % (
            pluralize(spins, 'is 1 spin', 'are %d spins' % spins)
        )

    def _get_whose_turn_message(self):
        return "It's %s turn." % apostrophize(self.game_state.get_current_player().name)

    def _prompt_yes_no(self, prompt):
        response = None

        while response != 'y' and response != 'n':
            sys.stdout.write(prompt)
            response = raw_input()

        return response == 'y'

    def _prompt_number(self, prompt):
        response = ''

        while not response.isdigit():
            sys.stdout.write(prompt)
            response = raw_input()

        return int(response)

if __name__ == '__main__':
    TextGUI.start()
