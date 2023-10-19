#!/usr/bin/python3
""" Start a Flask web application
"""
from flask import Flask

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


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
