# coding: utf-8
import os
from default import Config


class TestingConfig(Config):
    # App config
    TESTING = True

    # Disable csrf while testing
    WTF_CSRF_ENABLED = False

    # Db config
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or \
        'sqlite:///' + os.path.join(Config.PROJECT_DIR, 'db-test.sqlite')
