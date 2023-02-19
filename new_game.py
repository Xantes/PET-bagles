import sqlalchemy

from sqlalchemy import create_engine

import psycopg2
# from psycopg2 import _T_conn as pg_connection
from psycopg2 import Error
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from psycopg2.extras import NamedTupleCursor
from Modules import logging_setup


import logging

logging_setup()
logger = logging.getLogger(__name__)


def pgsql_connect(user: str, password: str, host: str, db: str):

    connection = False

    engine = create_engine(
        f"postgresql+psycopg2://{user}:{password}@{host}/{db}")

    try:
        connection = engine.connect()
    except Exception as error:
        logger.error(error)

    return connection


def db_exist(connection: psycopg2.connect, name: str) -> bool:
    result = False
    request = "select * from pg_database where datname = '{0}'".format(name)
    with connection.cursor(cursor_factory=NamedTupleCursor) as cursor:
        cursor.execute(request)
        if cursor.fetchone():
            result = True
            logger.info("Database {0} already exists".format(name))

    return result


def db_create(connection: psycopg2.connect, name: str) -> bool:
    result = False
    request = ('create database {0}'.format(name))
    with connection.cursor(cursor_factory=NamedTupleCursor) as cursor:
        try:
            cursor.execute(request)
            result = True
        except (Exception, Error) as error:
            logger.error(error)

    return result


def connection_close(connection):
    if connection:
        connection.close()
        logger.info("Connection with database closed")


def db_connect(connection: psycopg2.connection, name: str) -> bool:
    request = f"\c {name}"
    result = False
    with connection.cursor() as cursor:
        try:
            cursor.execute(request)
            result = True
        except (Exception, Error) as error:
            logger.error(error)

    return result


connection = pgsql_connect('admin', '1111', 'localhost')

if not db_exist(connection, 'bagles_db'):
    db_create(connection, 'bagles_db')
else:
    db_connect(connection, 'bagles_db')

connection_close(connection)
