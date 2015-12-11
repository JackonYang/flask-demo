# -*- coding:utf-8 -*-
import os
from default import Config


class DevelopmentConfig(Config):
    # App config
    DEBUG = True

    # SQLAlchemy config
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
        'sqlite:///' + os.path.join(Config.PROJECT_DIR, 'db-dev.sqlite')
