#!/usr/bin/python3
"""List states"""

from flask import Flask
from models import storage
from models.engine.db_storage import DBStorage
from models.engine.file_storage import FileStorage

#check if this is the right syntax to import storages
my_app = Flask(__name__)

@app.teardown_appcontext
def clear_session():
    """Clear session"""
    storage.close()

@my_app.route("/states_list", strict_slashes=False)
def display_states():
    """Display states"""
    if type(storage) is FileStorage:
        dic_of_states = storage.all(State)
    elif type(storage) is DBStorage:
        dic_of_states = storage.all("State")
    return (render_template('7-states_list.html', dics=dic_of_states))

if __name__ == '__main__':
    my_app.run(host='0.0.0.0', port=5000)
