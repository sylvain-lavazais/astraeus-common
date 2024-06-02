import os
import sys
from typing import List

import psycopg2
import structlog
from psycopg2.extras import DictCursor
from yoyo import get_backend, read_migrations

from . import db

SELECT_BODY = '''
SELECT * FROM astraeus.body
'''

PING_QUERY = 'SELECT 1'


class Database:
    _db_host: str
    _db_port: str
    _db_user: str
    _db_name: str
    _db_password: str
    _migration_folder: str

    def __init__(self, db_host: str, db_port: str, db_user: str, db_name: str, db_password: str):
        self._migration_folder = os.path.dirname(os.path.abspath(db.__file__))
        self._db_host = db_host
        self._db_port = db_port
        self._db_user = db_user
        self._db_name = db_name
        self._db_password = db_password
        self._log = structlog.get_logger()
        self.__try_connection(PING_QUERY)
        self.__apply_migration()
        self.__try_connection(SELECT_BODY)

    def __apply_migration(self):
        self._log.debug('applying yoyo migration')
        backend = get_backend(f'postgresql://{self._db_user}:{self._db_password}@'
                              f'{self._db_host}:{self._db_port}/{self._db_name}')
        self._log.debug(f'applying migration files in {self._migration_folder}')
        migrations = read_migrations(self._migration_folder)
        backend.apply_migrations(backend.to_apply(migrations))

    def __try_connection(self, query: str):
        with self.__db_connection() as connection:
            with connection.cursor(cursor_factory=DictCursor) as cursor:
                cursor.execute(query)

    def __db_connection(self):
        try:
            params = {
                'database': self._db_name,
                'user': self._db_user,
                'password': self._db_password,
                'host': self._db_host,
                'port': self._db_port
            }
            return psycopg2.connect(**params)
        except (Exception, psycopg2.DatabaseError) as error:
            self._log.critical(f'Error occur on connection to database - \n {error}')
            sys.exit(1)

    def exec_db_read(self, query: str, param: dict = None) -> List[dict]:
        log_query = query.replace('\n', '')
        try:
            with self.__db_connection() as connection:
                with connection.cursor(cursor_factory=DictCursor) as cursor:
                    cursor.execute(query, param)
                    self._log.debug(f'executing query [{log_query}]')
                    self._log.debug(f'with param [{param}]')
                    return cursor.fetchall()
        except psycopg2.DatabaseError as error:
            self._log.warn(f'Error occur on read of {log_query} - {error}')

    def exec_db_write(self, query: str, params: dict) -> None:
        log_query = query.replace('\n', '')
        try:
            with self.__db_connection() as connection:
                with connection.cursor() as cursor:
                    cursor.execute(query, params)
                    self._log.debug(f'executing query [{log_query}]')
                connection.commit()
        except psycopg2.DatabaseError as error:
            self._log.error(f'Error occur on write of {log_query} - {error}')
            connection.rollback()
