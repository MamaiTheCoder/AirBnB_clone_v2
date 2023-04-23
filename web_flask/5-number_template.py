#!/usr/bin/python3
"""
A script that starts a Flask web application.
"""

from flask import Flask, render_template

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


@app.route('/python/(<text>)')
@app.route('/python', defaults={'text': 'is cool'})
def python_page(text):
    """ Display “Python ”, followed by the value of the text variable.
    (replace underscore _ symbols with a space )
    """
    return 'Python {}'.format(text.replace('_', ' '))


@app.route('/number/<int: n>')
def num_only(n):
    """Display “n is a number” only if n is an integer."""
    return '{}'.format(n)


@app.route('/number_template/<n>')
def html_page():
    """Display a HTML page only if n is an integer."""
    ctxt = {
        'n': n
    }
    return render_template('5-number.html', **ctxt)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
