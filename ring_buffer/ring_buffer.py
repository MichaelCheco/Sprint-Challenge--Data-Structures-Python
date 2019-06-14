class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = 0
        self.storage = [None]*capacity
        self.pointer = 0
        self.count = 0

    def append(self, item):
        if self.count < self.capacity:
            self.storage.append(item)
            self.storage.pop(0)
            self.count += 1
        else:
            self.storage[self.pointer] = item
            self.pointer += 1
            if self.pointer == self.capacity:
                self.pointer = 0

    def get(self):
        return [item for item in self.storage if item is not None]
