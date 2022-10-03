from pickle import FALSE
from random import shuffle


class Generator():
    def __init__(self, max_letters=3, adv_mode=False) -> None:
        self.digit = list("0123456789")
        self.adv_digit = list("0123456789abcdef")
        self.max_letters = max_letters
        self.adv_mode = adv_mode

    def generate(self):
        if self.adv_mode:
            shuffle(self.adv_digit)
            return ''.join(self.adv_digit)[:self.max_letters]
        else:
            shuffle(self.digit)
            return ''.join(self.digit)[:self.max_letters]
