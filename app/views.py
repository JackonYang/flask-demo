# -*- Encoding: utf-8 -*-
from flask import Blueprint

bp = Blueprint('default', __name__)


@bp.route('/')
def index():
    return '<h1>Hello World!</h1>'


@bp.route('/user/<name>')
def user(name):
    return '<h1>Hello, %s!</h1>' % name
