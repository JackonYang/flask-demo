# -*- Encoding: utf-8 -*-
from flask import Flask


def make_app():
    app = Flask(__name__)
    registe_routes(app)
    return app


def registe_routes(app):
    """Register routes."""
    import views
    app.register_blueprint(views.bp)
    # print app.url_map
