import functools


@functools.total_ordering
class Data(object):
  def __init__(self, value=None):
    self.value = value

  def __eq__(self, other):
    return self.value == other.value

  def __lt__(self, other):
    return self.value < other.value
