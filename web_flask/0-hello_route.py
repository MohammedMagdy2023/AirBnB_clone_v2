#!/usr/bin/python3
"""
Create a flask web application for AirBNB project
"""
from flask import Flask
app = Flask(__name__)


@app.route("/")
def hello(strict_slashes=False):
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(host='0.0.0.0')
