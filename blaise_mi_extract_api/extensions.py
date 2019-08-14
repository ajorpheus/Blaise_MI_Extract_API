from flask_caching import Cache
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
import os

db = SQLAlchemy()
cache = Cache()


login_manager = LoginManager()
login_manager.login_message_category = "warning"


if 'mssql' in os.getenv('SQLALCHEMY_DATABASE_URI', ''):
    db.metadata.schema = 'BSM'
