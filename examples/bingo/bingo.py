import random


class Bingo:
    def __init__(self, items):
        self._items = list(items)
        random.shuffle(self._items)

    def pop(self):
        return self._items.pop()

    def __len__(self):
        return len(self._items)
