from PyQt4.QtCore import QTimer

class QuestionTimer(object):
    def __init__(self, events, game_state, opts):
        self.INTERVAL = 1000  # 1 second

        self.events = events
        self.game_state = game_state
        self.opts = opts
        self.current_ticks = 0

        self.timer = QTimer()
        self.timer.setInterval(self.INTERVAL)
        self.timer.timeout.connect(self._on_tick)

    def start(self):
        self.current_ticks = 0
        self._broadcast_tick()
        self.timer.start()

    def stop(self):
        self.timer.stop()

    # private

    def _on_tick(self):
        self.current_ticks += 1
        self._broadcast_tick()

        if self._has_expired():
            self.events.broadcast('question_timer.has_expired')
            self.stop()

    def _broadcast_tick(self):
        total = self._ticks_for_current_round()
        self.events.broadcast('question_timer.tick', total - self.current_ticks)

    def _has_expired(self):
        return self.current_ticks >= self._ticks_for_current_round()

    def _ticks_for_current_round(self):
        if self.game_state.current_round == 1:
            return self.opts.time_limit1
        else:
            return self.opts.time_limit2
