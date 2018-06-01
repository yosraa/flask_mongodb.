import os

basedir = os.path.abspath(os.path.dirname(__file__))


class BaseConfig(object):

    """Base configuration"""
    BCRYT_LOG = 4
    DEBUG_TB_ENABLED = False
    # SECRET_KEY


class DevelopmentConfig(BaseConfig):
      """ Development configuration."""
      DEBUG_TB_ENABLED = True
      WTF_CSRF_ENABLED = False
      DEBUG_TB_ENABLED = False
      MONGODB_DB = 'scoring_db'
      MONGODB_HOST = 'mongodb://127.0.0.1:27017/scoring_db'
      MONGODB_PORT = 27017

