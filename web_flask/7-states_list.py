#!/usr/bin/python3
""" Start a Flask web application
"""
from flask import Flask, render_template
from models import storage


app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def states_list():
    """ Display a HTML page for states_list """

    states = storage.all()
    for st in states:
        print(st)
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def close():
    """ Remove the current SQLAlchemy Session """
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
