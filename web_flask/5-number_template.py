#!/usr/bin/python3
""" Start a Flask web application
"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """ Route to display Hello HBNB! """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """ Route to display HBNB """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_is_fun(text):
    """ Route to display “C ” followed by the value of the text variable
        (replace underscore _ symbols with a space )
    """
    value = text.replace('_', ' ')

    return f'C {value}'


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_is_fun(text='is cool'):
    """ Route to display “Python” followed by the value of the text variable
        (replace underscore _ symbols with a space )
    """
    value = text.replace('_', ' ')

    return f'Python {value}'


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """ Display “n is a number” only if n is an integer
    """
    return f'{n} is a number'


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """ Display a HTML page only if n is an integer
    """
    return render_template('5-number.html', n=n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
