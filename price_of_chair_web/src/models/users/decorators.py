from functools import wraps

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
