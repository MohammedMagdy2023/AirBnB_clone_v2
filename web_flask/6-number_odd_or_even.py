#!/usr/bin/python3
"""
Create a flask web application for AirBNB project
"""
from flask import Flask, render_template
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hello_hbnb():
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_is(text):
    ntext = text.replace("_", " ")
    return f"C {ntext}"


@app.route("/python/", defaults={'text': 'is cool'}, strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_is(text):
    ntext = text.replace("_", " ")
    return f"Python {ntext}"


@app.route("/number/<int:n>", strict_slashes=False)
def hello_number(n):
    return f"{n} is a number"


@app.route("/number_template/<int:n>", strict_slashes=False)
def render_number(n):
    return render_template("5-number.html", n=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def even_or_odd(n):
    if n % 2 == 0:
        return render_template("6-number_odd_or_even.html", n=n, type="even")
    else:
        return render_template("6-number_odd_or_even.html", n=n, type="odd")


if __name__ == "__main__":
    app.run(host='0.0.0.0')
