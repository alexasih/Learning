from src.app import app


__author__ = 'alexasih'


app.run(debug=app.config['DEBUG'], port=4990)