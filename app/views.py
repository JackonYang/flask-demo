# -*- Encoding: utf-8 -*-
from flask import Blueprint, render_template,\
    session, redirect, url_for
from .forms import NameForm

bp = Blueprint('default', __name__)


@bp.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        session['name'] = form.name.data
        return redirect(url_for('default.index'))
    return render_template('default/index.html',
                           form=form, name=session.get('name'))


@bp.route('/user/<name>')
def user(name):
    return render_template('default/user.html', name=name)
