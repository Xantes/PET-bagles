class Checker():
    @staticmethod
    def check(word=None, test=None):
        word = str(word)
        test = str(test)
        result = []
        if word and test:
            for i, letter in enumerate(test):
                if word[i] == letter:
                    result.append('Pico')
                else:
                    if letter in word:
                        result.append('Fermi')
        if not result:
            result.append('Bagles')
        return result
