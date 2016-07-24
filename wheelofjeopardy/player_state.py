"""
Control and Monitor the wheelofjeopardy player
"""
class NoTokensAvailableError(Exception):
    pass

class PlayerState(object):
    def __init__(self, name, score=0, events):
        self.name = name
        self.events = events
        self.score = score # handicaps
        self.free_spin_tokens = 0

    def increase_score_by(self, amount):
        self.score += amount
        self._broadcast('score_did_update', self)

    def decrease_score_by(self, amount):
        self.score -= amount
        self._broadcast('score_did_update', self)

    def grant_free_spin_token(self):
        self.free_spin_tokens += 1
        self._broadcast('spin_tokens_did_update', self)

    def use_free_spin_token(self):
        if self.has_free_spin_token():
            self.free_spin_tokens -= 1
            self._broadcast('spin_tokens_did_update', self)
        else:
            raise NoTokensAvailableError('No free spin tokens available')

    def has_free_spin_token(self):
        return self.free_spin_tokens > 0

    # private

    def _broadcast(self, channel, *args):
        self.events.broadcast('player_state.%s' % channel, *args)
