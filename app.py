from Modules import Generator, Checker, CfgManager, language_factory
from Modules import logging_setup
import logging
import os


def main():
    logging_setup()
    logger = logging.getLogger(__name__)
    logger.info('App start')

    config_file = os.getenv('MAIN_CFG', None)
    config = CfgManager.load_conf(config_file)
    language_file = language_factory.provide_language(config['language'])
    language = CfgManager.load_conf(language_file)

    word = Generator(set=config['set'],
                     max_letters=config['max_letters']).generate()
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
    if not config['max_tries']:
        print(language['fail_msg'].format(word))

    logger.info('Game ends')

    print(language['final_msg'])


if __name__ == '__main__':
    main()
