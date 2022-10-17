import yaml
import logging
import os
from Modules import CfgManager
from Modules import logging_setup
import subprocess
import app


def main():
    logging_setup()
    logger = logging.getLogger(__name__)
    default_conf = {
        'New Game': 'app.py',
        'Records': 'records.py',
    }
    logger.info('Menu starts')
    config_file = os.getenv('MENU_CFG', None)
    config = CfgManager(cfg_file=config_file, default_conf=default_conf)

    while True:
        for key in config.config.keys():
            print(key)
        choice = input('menu> ')
        if choice == 'New Game':
            app.main()
        if choice == 'Exit':
            logger.info('Menu stops')
            break


if __name__ == '__main__':
    main()
