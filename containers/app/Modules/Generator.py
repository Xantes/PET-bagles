from random import shuffle


class Generator():
    def __init__(self, set: str = '0123456789', max_letters: int = 3):
        self.set = list(set)
        self.max_letters = max_letters

    def generate(self):
        shuffle(self.set)
        return ''.join(self.set)[:self.max_letters]
