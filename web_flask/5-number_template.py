#!/usr/bin/python3
"""
scripts to starts a Flask
"""

from flask import Flask, escape, render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """function to return Hello HBNB!"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hello():
    """ function to display HBNB"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def ctext(text):
    """ function to display C + value of text """
    text = text.replace("_", " ")
    return 'C {}'.format(escape(text))


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def pytext(text="is_cool"):
    """ function to display Python + value of text """
    text = text.replace("_", " ")
    return 'Python {}'.format(escape(text))


@app.route('/number/<int:n>', strict_slashes=False)
def num(n):
    """ function to display integers """
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def numberhtml(n):
    return render_template('5-number.html', num=n)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
