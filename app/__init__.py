# -*- Encoding: utf-8 -*-
from flask import Flask
from flask.ext.migrate import Migrate
from .models import db  # sql


def make_app():
    app = Flask(__name__)

    # used by flask-wtf for CSRF protection
    app.config['SECRET_KEY'] = 'hard to guess string'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
    app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

    db.init_app(app)
    migrate = Migrate(app, db)  # noqa

    registe_routes(app)
    return app


def registe_routes(app):
    """Register routes."""
    import views
    app.register_blueprint(views.bp)
    # print app.url_map
