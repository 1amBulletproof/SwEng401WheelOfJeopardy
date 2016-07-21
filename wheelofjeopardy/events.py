class Events(object):
  def __init__(self):
    self.subscriptions = {}

  def on(self, channel, func):
    if channel in self.subscriptions:
      self.subscriptions[channel].append(func)
    else:
      self.subscriptions[channel] = [func]

  def broadcast(self, channel, *args):
    if channel in self.subscriptions:
      for func in self.subscriptions[channel]:
        func(*args)
