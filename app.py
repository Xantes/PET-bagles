from Modules import Generator, Checker, CfgManager


def main():
    config_file = 'settings/main.yaml'
    config = CfgManager.load_conf(config_file)

    word = Generator(config['max_digit']).generate()
    print(
        f"Hello. There is Bagles game. You have to guess hidden number. You have only {config['max_tries']} tries. Have a luck")
    while True and config['max_tries']:
        if config['max_tries'] == 1:
            print(f"You have last try")
        else:
            print(f"You have {config['max_tries']} tries")
        test = input('> ')
        result = Checker.check(word, test)
        if result == ['Pico', 'Pico', 'Pico']:
            print(f"You won with {10 - config['max_tries']} tries")
            break
        else:
            print(result)
            config['max_tries'] -= 1
    print(f"Guessed number was {word}")
    print("Thanks for game")


if __name__ == '__main__':
    main()
