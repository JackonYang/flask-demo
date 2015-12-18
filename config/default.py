# -*- coding:utf-8 -*-
import os
from os.path import dirname, abspath

# make sure that calc abspath before dirname
_PROJECT_DIR = dirname(dirname(abspath(__file__)))


class Config(object):
    """base class for config"""
    SECRET_KEY = os.environ.get('SECRET_KEY') or \
        'FLASK_DEMO_BY_JACKON-.-www.jackon.me'
    PROJECT_DIR = _PROJECT_DIR

    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    @staticmethod
    def init_app(app):
        pass
