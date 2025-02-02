#!/usr/bin/python3
""" Start a Flask web application
"""
from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.route("/states", strict_slashes=False)
def states():
    """ Display a HTML page for states_list """
    states = storage.all(State)
    return render_template('9-states.html', states=states)


@app.route("/states/<id>", strict_slashes=False)
def state(id):
    """ Display a HTML page for states_list """
    state = storage.all(State).get(f'State.{id}')
    return render_template('9-states.html', state=state)


@app.teardown_appcontext
def teardown(self):
    """ Remove the current SQLAlchemy Session """
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
