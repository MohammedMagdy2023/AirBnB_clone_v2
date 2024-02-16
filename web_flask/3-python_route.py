#!/usr/bin/python3
"""
Create a flask web application for AirBNB project
"""
from flask import Flask
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hello_hbnb():
    return "HBNB"


@app.route("/c/<text>", , strict_slashes=False)
def c_is(text):
    ntext = text.replace("_", " ")
    return f"C {ntext}"


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route("/python/<text>", , strict_slashes=False)
def python_is(text):
    ntext = text.replace("_", " ")
    return f"Python {ntext}"


if __name__ == "__main__":
    app.run(host='0.0.0.0')