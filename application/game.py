from application.db import db, Sessions
from Modules import CfgManager, Generator, language_factory
from Modules import logging_setup
import logging
from application.app import app

import secrets

logging_setup()
logger = logging.getLogger(__name__)
logger.info('App start')

default_conf = {
    'max_letters': 3,
    'max_tries': 10,
    'adv_mode': False,
    'set': '1234567890',
    'language': 'English',
}


def create_new_game():
    cfg = CfgManager(
        cfg_file=app.config['MAIN_CFG'], default_conf=default_conf)
    session_id = secrets.token_hex(nbytes=16)

    number = Generator(set=cfg.config['set'],
                       max_letters=cfg.config['max_letters']).generate()

    session = Sessions(
        session_id=session_id,
        user=None,
        number=number,
        tries=cfg.config['max_tries'],
        finish=False)

    db.session.add(session)
    db.session.commit()

    return session_id
