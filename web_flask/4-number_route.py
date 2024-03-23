#!/usr/bin/python3
"""Display different message when route /, /hbnb specified"""
from flask import Flask
my_app = Flask(__name__)


@my_app.route("/", strict_slashes=False)
def display_hello():
    """Display message"""
    return ("Hello HBNB!")


@my_app.route("/hbnb", strict_slashes=False)
def display_hbnb():
    """Display message"""
    return ("HBNB")


@my_app.route("/c/<text>", strict_slashes=False)
def display_text(text):
    """Display message"""
    text = text.replace("_", " ")
    str = "C {}".format(text)
    return (str)


@my_app.route("/python/<text>", strict_slashes=False)
def display_def1(text):
    """Display message"""
    text = text.replace("_", " ")
    str = "Python {}".format(text)
    return (str)


@my_app.route("/python", strict_slashes=False)
def display_def2():
    """Display message"""
    return ("Python is cool")


@my_app.route("/python/", strict_slashes=False)
def display_def3():
    """Display message"""
    return ("Python is cool")


@my_app.route("/number/<int:n>", strict_slashes=False)
def display_n(n):
    """Display message"""
    str = "{} is a number".format(n)
    return (str)


if __name__ == '__main__':
    my_app.run(host='0.0.0.0', port=5000)
