#!/usr/bin/python3
'''Display messages based on specified app route'''
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


if __name__ == '__main__':
    my_app.run(host='0.0.0.0', port=5000)
