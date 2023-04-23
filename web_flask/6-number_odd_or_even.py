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

@app.route('/python/')
@app.route('/python/<text>')
def python_text(text='is cool'):
    """ Display “Python ”, followed by the value of the text variable.
    (replace underscore _ symbols with a space )
    """
    if text is not 'is cool':
        text = text.replace('_', ' ')
    return 'Python %s' % text


@app.route('/number/<int:n>')
def number(n):
    """ Display a HTML page only if n is an integer."""
    return "%d is a number" % n


@app.route('/number_template/<int:n>')
def number_template(n):
    """ Display a HTML page only if n is an integer."""
    return render_template('5-number.html', number=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    """ Display a HTML page only if n is an integer."""
    return render_template('6-number_odd_or_even.html', number=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
