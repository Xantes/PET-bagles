from yaml import safe_load
import logging
from pathlib import Path
from typing import Dict, Any


class CfgManager():
    def __init__(self, cfg_file: str = '', default_conf: Dict[Any, Any] = {}) -> None:
        self.config: Dict[Any, Any] = {}
        self.default_conf: Dict = default_conf
        self.logger = logging.getLogger(__name__)
        if cfg_file:
            if Path(cfg_file).exists():
                self.load_conf(cfg_file)
            else:
                self.logger.error(
                    "Config file doesn't exist. Load default configuration")
                self.load_default_conf()
        else:
            self.logger.error("Config doesn't set. Used default")
            self.load_default_conf()

    def load_default_conf(self):
        if not self.config:
            self.config = self.default_conf

    def load_conf(self, file):
        try:
            with open(file, 'r') as r_file:
                if self.config:
                    r_cfg = safe_load(r_file)
                    for key, value in r_cfg.items():
                        self.config[key] = value
                else:
                    self.config = safe_load(r_file)

                self.logger.info(f"Config_file: {file} succefully load")
        except OSError as exception:
            self.logger.error(exception)
            self.load_default_conf()
