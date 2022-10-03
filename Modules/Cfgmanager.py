from yaml import safe_load
import sys


class CfgManager():
    @staticmethod
    def load_conf(file):
        try:
            with open(file, 'r') as r_file:
                config = safe_load(r_file)
        except OSError as exception:
            sys.exit(exception)
        return config
