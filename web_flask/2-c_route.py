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


@app.route("/c/<text>")
def c_is(text):
    ntext = text.replace("_", " ")
    return f"C {ntext}"


if __name__ == "__main__":
    app.run(host='0.0.0.0')