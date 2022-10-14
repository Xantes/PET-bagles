from yaml import safe_load
import sys
import logging
import os


class CfgManager():
    @staticmethod
    def load_conf(file):
        logger = logging.getLogger(__name__)
        if os.path.exists(file):
            try:
                with open(file, 'r') as r_file:
                    config = safe_load(r_file)
                    logger.info(f"Config_file: {file} succefully load")
            except OSError as exception:
                logger.error(exception)
                sys.exit(exception)
            return config
        else:
            logger.error(f'File {file} not found')
            sys.exit(1)
