from application.db import db, Sessions, Languages
from Modules import CfgManager, Generator, language_factory, Checker
from Modules import logging_setup
import logging
from application.app import app
from flask import session

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


def another_try(session_id, try_number) -> dict:
    sql_response = Sessions.query.filter_by(session_id=session_id).first()

    checker = list()
    results = dict()

    if sql_response.tries and not sql_response.finish:
        sql_response.tries = sql_response.tries - 1
        if sql_response.number == try_number:
            sql_response.finish = True
        elif sql_response.tries:
            checker = Checker.check(
                sql_response.number, try_number)

        db.session.commit()

    results = dict(
        is_finish=sql_response.finish,
        tries=sql_response.tries,
        message=make_message(sql_response),
        checker_response=checker,
    )

    return results


def make_message(sql_response: Sessions) -> str:
    message = str()
    # language_response = Languages.query.filter_by(
    #     language=session['language']).first()

    if sql_response.finish and sql_response.tries:
        message = f'Congratulations. You won the game with {10 - sql_response.tries} tries'
    elif not sql_response.finish and not sql_response.tries:
        message = f'Sorry, but you lose. Guessed number was {sql_response.number}'
    elif sql_response.tries == 1:
        message = 'This is last try'

    return message
