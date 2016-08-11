from wheelofjeopardy.events import Events

class TestEvents(Events):
    def __init__(self):
        self.reset()
        super(TestEvents, self).__init__()

    def broadcast(self, channel, *args):
        self.broadcasts.append(channel)
        super(TestEvents, self).broadcast(channel, *args)

    def did_broadcast(self, channel, times=1):
        count = 0

        for broadcast_channel in self.broadcasts:
            if broadcast_channel == channel:
                count += 1

        return times == count

    def reset(self):
        self.broadcasts = []
