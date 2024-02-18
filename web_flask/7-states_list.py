#!/usr/bin/pyhon3
"""
Flask Web Application for the AirBNB project
"""
from flask import Flask, render_template
from models import *
from models import storage
app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def states_list():
    """Display a list of states in the database."""
    states = sorted(list(storage.all("State").values()), key=lambda st: st.name)
    return render_template("7-states_list.html", states=states)


@app.teardown_appcontext
def teardown(exc):
    """Remove the current SQLAlchemy session."""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0")
