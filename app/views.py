# -*- Encoding: utf-8 -*-
from flask import Blueprint, render_template

bp = Blueprint('default', __name__)


@bp.route('/')
def index():
    return render_template('default/index.html')


@bp.route('/user/<name>')
def user(name):
    return render_template('default/user.html', name=name)
