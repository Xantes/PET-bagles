import os
import yaml
import logging.config
import logging


def logging_setup(default_path='settings\log.yml', default_level=logging.INFO, env_key='LOG_CFG'):
    value = os.getenv(env_key, None)
    if value:
        default_path = value
    if os.path.exists(default_path):
        with open(default_path, 'r') as r_file:
            try:
                config = yaml.safe_load(r_file)
                logging.config.dictConfig(config)
            except Exception as e:
                print(e)
                print('Error in Logging configuration. Used default')
                logging.basicConfig(level=default_level)
    else:
        logging.basicConfig(level=default_level)
        print('Failed to load configuration file. Using default settings')
