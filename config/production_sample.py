# coding: utf-8
import os
from default import Config


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'mysql://root:password@localhost:3306/database'
