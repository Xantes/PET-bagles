from Modules import Generator, Checker, CfgManager, language_factory


def main():
    config_file = 'settings/main.yaml'
    config = CfgManager.load_conf(config_file)
    language_file = language_factory.provide_language(config['language'])
    language = CfgManager.load_conf(language_file)

    word = Generator(config['max_digit']).generate()
    print(language['hello_msg'].format(config['max_tries']))
    while True and config['max_tries']:
        if config['max_tries'] == 1:
            print(language['last_try'])
        else:
            print(language['tries_count'].format(config['max_tries']))
        test = input('> ')
        if test == word:
            print(language['win_msg'].format(10 - config['max_tries']))
            break
        else:
            result = Checker.check(word, test)
            print(result)
            config['max_tries'] -= 1
    print(language['fail_msg'].format(word))
    print(language['final_msg'])


if __name__ == '__main__':
    main()
