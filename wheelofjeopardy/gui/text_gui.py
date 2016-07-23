import sys
import os

# make sure wheelofjeopardy module is available on the load path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

from wheelofjeopardy.events import Events
from wheelofjeopardy.player_state import PlayerState
from wheelofjeopardy.game_state import GameState
from wheelofjeopardy.text_helper import apostrophize, pluralize

class TextGUI(object):
    @classmethod
    def start(cls):
        print 'Welcome to Wheel of Jeopardy!'
        print "Let's get started!"

        events = Events()
        TextGUI(cls._create_game_state(events), events)._start()

    # private static

    @classmethod
    def _create_game_state(cls, events):
        player1 = cls._create_player("Enter first player's name: ", events)
        player2 = cls._create_player("Enter second player's name: ", events)
        return GameState([player1, player2], events)

    @classmethod
    def _create_player(cls, message, events):
        sys.stdout.write(message)
        return PlayerState(name=raw_input(), events=events)

    # public instance

    def __init__(self, game_state, events):
        self.game_state = game_state
        self.events = events

    # private instance

    def _start(self):
        self.events.on('game_state.current_player_did_change', self._on_current_player_did_change)
        self.events.on('game_state.spins_did_update', self._on_spins_did_update)
        self.events.on('game_state.turn_will_end', self._on_turn_will_end)

        while self.game_state.any_spins_remaining():
            print 'What would you like to do, %s?' % self.game_state.get_current_player().name
            sys.stdout.write("(S)pin, (Q)uit, (P)rint scores: ")
            answer = raw_input().lower()

            if answer == 's':
                self.game_state.spin()
            elif answer == 'p':
                self._print_scores()
            elif answer == 'q':
                break

        print 'Good game!'

    def _on_current_player_did_change(self, game_state):
        print self._get_whose_turn_message()

    def _on_spins_did_update(self, game_state):
        print self._get_spins_remaining_message()

    def _on_turn_will_end(self, game_state):
        print 'That concludes %s turn.' % apostrophize(game_state.get_current_player().name)

    def _print_scores(self):
        score_strings = []

        for player_state in self.game_state.player_states:
            score_strings.append("%s has %d points" % (player_state.name, player_state.score))

        print 'Here are the scores:'
        print ', '.join(score_strings)

    def _get_spins_remaining_message(self):
        spins = self.game_state.spins_remaining

        return "There %s remaining." % (
            pluralize(spins, 'is 1 spin', 'are %d spins' % spins)
        )

    def _get_whose_turn_message(self):
        return "It's %s turn." % apostrophize(self.game_state.get_current_player().name)

if __name__ == '__main__':
    TextGUI.start()
