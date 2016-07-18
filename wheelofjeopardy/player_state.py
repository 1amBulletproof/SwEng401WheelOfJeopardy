class NoTokensAvailableError(Exception):
  pass

class PlayerState(object):
  def __init__(self, name):
    self.name = name
    self.score = 0
    self.free_spin_tokens = 0

  def increase_score_by(self, amount):
    self.score += amount

  def decrease_score_by(self, amount):
    self.score -= amount

  def grant_free_spin_token(self):
    self.free_spin_tokens += 1

  def use_free_spin_token(self):
    if self.has_free_spin_token():
      self.free_spin_tokens -= 1
    else:
      raise NoTokensAvailableError('No free spin tokens available')

  def has_free_spin_token(self):
    return self.free_spin_tokens > 0
