class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = 0
        self.storage = [None]*capacity

    def _increment_current(self):
        self.current = (self.current + 1) % self.capacity

    def append(self, item):
        self.storage[self.current] = item
        self._increment_current()

    def get(self):
        return [i for i in self.storage if i is not None]
