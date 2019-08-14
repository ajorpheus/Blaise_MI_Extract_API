from flask import Flask
from blaise_mi_extract_api.views import api_view

import os
from blaise_mi_extract_api.extensions import (
    cache,
    login_manager,
    db,
)


def create_app(object_name=None):

    app = Flask(__name__, instance_relative_config=True)

    # use system env settings these may be overwritten by config files settings
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI', '')
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', '')
    app.config['LDAP_SERVER'] = os.getenv('LDAP_SERVER', '')
    app.config['ENV'] = os.getenv('ENV', '')

    # set app variables
    app.config.from_object(object_name)
    if not object_name:
        app.config.from_pyfile('config.py')

    # initialize extensions
    cache.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)

    # register blueprints
    app.register_blueprint(api_view)

    return app
