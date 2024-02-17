#!/usr/bin/pyhon3
"""
Flask Web Application for the AirBNB project
"""
from flask import Flask, render_template
from models import storage
app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def states_list():
    states = storage.all("State")
    return render_template("7-states_list.html", states)


@app.teardown_appcontext()
def end_of_app():
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0")
