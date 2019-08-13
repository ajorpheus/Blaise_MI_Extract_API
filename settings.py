import tempfile
db_file = tempfile.NamedTemporaryFile()


class Config(object):
    SECRET_KEY = 'add_key_here'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    CACHE_NO_NULL_WARNING = True
    USERS_PER_PAGE = 10