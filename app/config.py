'''This module defines Flask app configuration options.'''
from enum import Enum

class _BaseConfig:
    pass

class _DevelopmentConfig(_BaseConfig):
    DEBUG = True
    SEND_FILE_MAX_AGE_DEFAULT = 0  # Do not cache static files on client
    MONGODB_HOST = '127.0.0.1'
    MONGODB_PORT = 27017
    MONGODB_DB = 'bookmarkswtf-dev'

class _TestingConfig(_BaseConfig):
    TESTING = True

class _ProductionConfig(_BaseConfig):
    pass

class Config(Enum):
    '''This class contains separate Flask configs for development, testing and production.'''

    DEVELOPMENT = _DevelopmentConfig()
    TESTING = _TestingConfig()
    PRODUCTION = _ProductionConfig()

    DEFAULT = DEVELOPMENT
