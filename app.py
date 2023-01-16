from Modules import Generator, Checker, CfgManager, language_factory
from Modules import logging_setup
import logging
import os


def main():
    logging_setup()
    logger = logging.getLogger(__name__)
    logger.info('App start')

    config_file = os.getenv('MAIN_CFG', None)
    default_conf = {
        'max_letters': 3,
        'max_tries': 10,
        'adv_mode': False,
        'set': '1234567890',
        'language': 'English',
    }
    cfg = CfgManager(cfg_file=config_file, default_conf=default_conf)
    language_file = language_factory.provide_language(cfg.config['language'])
    cfg.load_conf(language_file)

    word = Generator(set=cfg.config['set'],
                     max_letters=cfg.config['max_letters']).generate()
    print(cfg.config['hello_msg'].format(cfg.config['max_tries']))
    while True and cfg.config['max_tries']:
        if cfg.config['max_tries'] == 1:
            print(cfg.config['last_try'])
        else:
            print(cfg.config['tries_count'].format(cfg.config['max_tries']))
        test = input('> ')
        if test == word:
            print(cfg.config['win_msg'].format(10 - cfg.config['max_tries']))
            break
        else:
            result = Checker.check(word, test)
            print(result)
            cfg.config['max_tries'] -= 1
    if not cfg.config['max_tries']:
        print(cfg.config['fail_msg'].format(word))

    logger.info('Game ends')

    print(cfg.config['final_msg'])


if __name__ == '__main__':
    main()
