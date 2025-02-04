#!/usr/bin/python3
"""
A script that starts a Flask web application.
"""

from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def index():
    """Displays “Hello HBNB!”"""
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    """Dislays “HBNB”."""
    return 'HBNB'


@app.route('/c/<text>')
def c_pg(text):
    """Display “C ” followed by the value of the text variable.
    (replace underscore _ symbols with a space )
    """
    return 'C {}'.format(text.replace('_', ' '))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
