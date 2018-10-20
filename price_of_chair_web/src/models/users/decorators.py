from functools import wraps

__author__ = 'alexasih'


def requires_login(func):
    @wraps(func)
    def decorated_function():
        print("Hi")
        return func(*args, **kwargs)  # func(...) args: func(5, 6) kwargs: (x=5,y=6)
    return decorated_function


@requires_login
def my_function(x, y):
    return x+y

my_function()