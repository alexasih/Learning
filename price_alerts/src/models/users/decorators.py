from functools import wraps

from src import config
from src.app import app

from flask import url_for, session, request
from werkzeug.utils import redirect

__author__ = 'alexasih'


def require_login(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        if 'email' not in session.keys() or session['email'] is None:
            return redirect(url_for('users.login_user', next=request.path))
        return func(*args, **kwargs)
    return decorated_function


def requires_admin_permissions(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        if 'email' not in session.keys() or session['email'] is None:
            return redirect(url_for('users.login_user', next=request.path))
        if session['email'] not in app.config['ADMINS']:
            return redirect(url_for('users.login_user'))
        return func(*args, **kwargs)
    return decorated_function
