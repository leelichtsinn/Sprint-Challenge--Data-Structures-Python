class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.current = 0
    self.storage = [None]*capacity

  def append(self, item):
    # check storage > capacity
    if self.storage > self.capacity:
        self.storage.pop([0])
        self.storage.append(item)

    self.storage.append(item)

  def get(self):
    pass
