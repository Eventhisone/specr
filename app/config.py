"""Flask config class."""
import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    """Set Flask configuration vars."""

    # General Config
    TESTING = os.environ.get('APP_TESTING')
    DEBUG = os.environ.get('APP_DEBUG')
    SECRET_KEY = os.environ.get('APP_SECRET_KEY')
    SESSION_COOKIE_NAME = os.environ.get('ASPIRATIONS_COOKIE_NAME')
    FLASK_ENV = os.environ.get('APP_ENV')
   
    # Database
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_USERNAME = os.environ.get('SQLALCHEMY_DATABASE_USER')
    SQLALCHEMY_PASSWORD = os.environ.get('SQLALCHEMY_DATABASE_PASS')
    SQLALCHEMY_DATABASE_NAME = os.environ.get('SQLALCHEMY_DATABASE_NAME')
    SQLALCHEMY_TABLE = os.environ.get('SQLALCHEMY_DATABASE_MIGRATION_TABLE')
    SQLALCHEMY_DB_SCHEMA = os.environ.get('SQLALCHEMY_DATABASE_SCHEMA')
    SQLALCHEMY_TRACK_MODIFICATIONS = os.environ.get('SQLALCHEMY_TRACK_MODS')
