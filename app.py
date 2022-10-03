from Modules import Generator, Checker


def main():
    MAX_LETTERS = 3
    MAX_TRIES = 10
    ADV_MODE = False

    word = Generator(MAX_LETTERS).generate()
    print(
        f"Hello. There is Bagles game. You have to guess hidden number. You have only {MAX_TRIES} tries. Have a luck")
    while True and MAX_TRIES:
        if MAX_TRIES == 1:
            print(f"You have last try")
        else:
            print(f"You have {MAX_TRIES} tries")
        test = input('> ')
        result = Checker.check(word, test)
        if result == ['Pico', 'Pico', 'Pico']:
            print(f"You won with {10 - MAX_TRIES} tries")
            break
        else:
            print(result)
            MAX_TRIES -= 1
    print(f"Guessed number was {word}")
    print("Thanks for game")


if __name__ == '__main__':
    main()
