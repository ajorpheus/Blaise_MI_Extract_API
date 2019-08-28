import tempfile
db_file = tempfile.NamedTemporaryFile()


class Config(object):
    SECRET_KEY = '123456'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    CACHE_NO_NULL_WARNING = True
    USERS_PER_PAGE = 10


class TestConfig(Config):
    ENV = 'test'
    DEBUG = True
    DEBUG_TB_ENABLED = False
    DEBUG_TB_INTERCEPT_REDIRECTS = False

    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    SQLALCHEMY_ECHO = True

    CACHE_TYPE = 'null'
    WTF_CSRF_ENABLED = False