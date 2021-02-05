# standard
import os
from configparser import ConfigParser
# external
from sqlalchemy import create_engine


def get_engine():
    if not os.access('settings.ini', 4):
        raise Exception('settings.ini not found!')
    c = ConfigParser()
    c.read('settings.ini')
    db = c['database']
    dburl = 'mysql+mysqlconnector://{}:{}@{}/{}'.format(db['user'], db['password'], db['host'], db['dbname'])
    return create_engine(dburl)

