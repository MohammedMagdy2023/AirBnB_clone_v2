#!/usr/bin/pyhon3
"""
Flask Web Application for the AirBNB project
"""
from flask import Flask, render_template
from models import storage
app = Flask(__name__)


@app.route("/cities_by_states", strict_slashes=False)
@app.route('/states/<state_id>', strict_slashes=False)
def statesState():
    """Display a list of states in the database."""
    states = storage.all("State")
    if state_id is not None:
        state_id = 'State.' + state_id
    return render_template('9-states.html', states=states, state_id=state_id)


@app.teardown_appcontext
def teardown(exc):
    """Remove the current SQLAlchemy session."""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0")
