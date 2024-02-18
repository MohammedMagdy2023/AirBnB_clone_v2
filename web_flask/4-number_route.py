#!/usr/bin/python3
"""
Create a flask web application for AirBNB project
"""
from flask import Flask
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """Return Hello HBNB! on the main URL"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hello_hbnb():
    """Return HBNB on the /hbnb URL"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_is(text):
    """Return C <text> on the /c URL"""
    ntext = text.replace("_", " ")
    return f"C {ntext}"


@app.route("/python/", defaults={'text': 'is cool'}, strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_is(text):
    """Return Python <text> on the /python URL"""
    ntext = text.replace("_", " ")
    return f"Python {ntext}"


@app.route("/number/<int:n>", strict_slashes=False)
def hello_number(n):
    """Return n is a number if n is an integer"""
    return f"{n} is a number"


if __name__ == "__main__":
    app.run(host='0.0.0.0')
