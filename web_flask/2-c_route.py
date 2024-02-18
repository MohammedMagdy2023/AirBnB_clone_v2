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


@app.route("/c/<text>")
def c_is(text):
    """Return C followed by the value of the text variable"""
    ntext = text.replace("_", " ")
    return f"C {ntext}"


if __name__ == "__main__":
    app.run(host='0.0.0.0')
