#!/usr/bin/python3
"""Renders html file based on routes specified"""

from flask import Flask, render_template
from models.engine.db_storage import DBStorage
from models.engine.file_storage import FileStorage

my_app = Flask(__name__)


@my_app.teardown_appcontext
def clear_session(exception=None):
    """Clear session in case of end of request."""
    from models import storage
    models.storage.close()


@my_app.route("/states_list", strict_slashes=False)
def display_states():
    """Display states when route is passed to application."""
    if type(models.storage) is FileStorage:
        dic_of_states = models.storage.all(State)
    elif type(models.storage) is DBStorage:
        dic_of_states = models.storage.all("State")
    print(dic_of_states)
    dics = [obj for obj in dic_of_states.values()]
    return (render_template('7-states_list.html', dics=dics))


if __name__ == '__main__':
    """Listen at a particular IP and port."""
    my_app.run(host='0.0.0.0', port=5000)
