import sys
import os

from wheelofjeopardy.events import Events
from wheelofjeopardy.player_state import PlayerState
from wheelofjeopardy.game_state import GameState
from wheelofjeopardy.text_helper import apostrophize, pluralize
from wheelofjeopardy.utils.read_configs import ReadCfgToOptions

class TextGUI(object):
    @classmethod
    def start(cls):
        print 'Welcome to Wheel of Jeopardy!'
        print "Let's get started!"
        global opts

        events = Events()
        opts = ReadCfgToOptions()
        TextGUI(cls._create_game_state(events), events)._start()

    # private static

    @classmethod
    def _create_game_state(cls, events):
        players = [PlayerState(opts.playerNames[n], events, opts.startScores[n])
                   for n in range(opts.nPlayers)]
        return GameState(players, events, opts)

    @staticmethod
    def _clear_terminal():
        raw_input("Press Enter to continue...")
        os.system('cls' if os.name=='nt' else 'clear')

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
        self.events.subscribe('opponent_choice_sector.choose_category', self._on_prompt_for_category)
        self.events.subscribe('player_choice_sector.choose_category', self._on_prompt_for_category)

        self.events.subscribe('board_sector.question_will_be_asked', self._on_question_will_be_asked)
        self.events.subscribe('board_sector.check_answer', self._on_check_answer)
        self.events.subscribe('sector.prompt_for_token_use', self._on_prompt_for_token_use)
        self.events.subscribe('sector.no_questions_in_category', self._on_no_questions_in_category)

        TextGUI._clear_terminal()
        while not self.game_state.has_game_ended():
            print(self.game_state.board)
            print 'What would you like to do, %s?' % \
                self.game_state.get_current_player().name
            sys.stdout.write("(S)pin, (Q)uit, (P)rint scores: ")
            answer = raw_input().lower()

            if answer == 's':
                self.game_state.spin()
            elif answer == 'p':
                self._print_scores()
            elif answer == 'q':
                break
            elif len(answer)>0 and answer[0] == 'c': # cheat menu
                self.game_state._cheat(answer[1:])

            if self.game_state.has_round_ended(): # if round ended, go to next
                self.events.broadcast('gui.round_did_end')
                self._print_scores() # print end-of-round score

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
        print "Alright, here's the %d-point question in %s:" % (question[0], question[1])
        sys.stdout.write('%s: ' % (question[2].text))
        answer = raw_input()
        self.events.broadcast('gui.answer_received', answer)

    def _on_check_answer(self, question, answer):
        player_name = self.game_state.get_current_player().name
        print 'Correct answer is: %s' % (question[2].answer)
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

    def _print_scores(self):
        score_strings = []

        for pl in self.game_state.player_states:
            score_strings.append("\t%s has %u points, %u tokens." % \
                                 (pl.name, pl.score, pl.free_spin_tokens) )

        print 'Here are the scores:'
        print '\n'.join(score_strings)
        TextGUI._clear_terminal()

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

if __name__ == '__main__':
    TextGUI.start()
