# -*- Encoding: utf-8 -*-
from flask import Flask
from flask.ext.migrate import Migrate
from config import load_config, load_default
from .models import db  # sql


def make_app(config_name):
    app = Flask(__name__)

    config_obj = load_config(config_name)
    if not config_obj:
        print 'load default config instead.'
        config_obj = load_default()
    app.config.from_object(config_obj)
    config_obj.init_app(app)

    db.init_app(app)
    migrate = Migrate(app, db)  # noqa

    registe_routes(app)
    return app


def registe_routes(app):
    """Register routes."""
    import views
    app.register_blueprint(views.bp)
    # print app.url_map
