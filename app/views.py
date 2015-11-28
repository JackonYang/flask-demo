# -*- Encoding: utf-8 -*-
from flask import Blueprint, render_template
from .forms import NameForm

bp = Blueprint('default', __name__)


@bp.route('/', methods=['GET', 'POST'])
def index():
    name = None
    form = NameForm()
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
    return render_template('default/index.html',
                           form=form, name=name)


@bp.route('/user/<name>')
def user(name):
    return render_template('default/user.html', name=name)
