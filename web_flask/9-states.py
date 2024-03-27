#!/usr/bin/python3
"""List states"""

import models
from flask import Flask, render_template
from models.engine.db_storage import DBStorage
from models.engine.file_storage import FileStorage

my_app = Flask(__name__)


@my_app.teardown_appcontext
def clear_session(exception=None):
    """Clear session"""
    models.storage.close()


@my_app.route("/states_list", strict_slashes=False)
def display_states():
    """Display states"""
    if type(models.storage) is FileStorage:
        dic_of_states = models.storage.all(State)
    elif type(models.storage) is DBStorage:
        dic_of_states = models.storage.all("State")
    dics = [obj for obj in dic_of_states.values()]
    return (render_template('7-states_list.html', dics=dics))


@my_app.route("/cities_by_states", strict_slashes=False)
def display_cities():
    """Display Cities"""
    if type(models.storage) is FileStorage:
        dic_of_states = models.storage.all(State)
        dic_of_cities = models.storage.all(City)
    elif type(models.storage) is DBStorage:
        dic_of_states = models.storage.all("State")
        dic_of_cities = models.storage.all("City")
    dics = [obj for obj in dic_of_states.values()]
    dicc = [obj for obj in dic_of_cities.values()]
    return (render_template('8-cities_by_states.html', dics=dics, dicc=dicc))


@my_app.route("/states", strict_slashes=False)
def display_states_2():
    """Display only states"""
    if type(models.storage) is FileStorage:
        dic_of_states = models.storage.all(State)
        dic_of_cities = models.storage.all(City)
    elif type(models.storage) is DBStorage:
        dic_of_states = models.storage.all("State")
        dic_of_cities = models.storage.all("City")
    dicc = [object for object in dic_of_cities.values()]
    dics = [obj for obj in dic_of_states.values()]
    obj = None
    return (render_template('9-states.html', det=1, st=obj, dicc=dicc,
            dics=dics))


@my_app.route("/states/<id>", strict_slashes=False)
def display_in_state(id):
    """Display cities under state given id"""
    if type(models.storage) is FileStorage:
        dic_of_states = models.storage.all(State)
        dic_of_cities = models.storage.all(City)
    elif type(models.storage) is DBStorage:
        dic_of_states = models.storage.all("State")
        dic_of_cities = models.storage.all("City")
    dicc = [object for object in dic_of_cities.values()]
    dics = [obj for obj in dic_of_states.values()]
    for state_obj in dic_of_states.keys():
        print(id)
        print(dic_of_states[state_obj].id)
        if str(dic_of_states[state_obj].id) == str(id):
            obj = dic_of_states[state_obj]
            break
    else:
        return (render_template('9-states.html', det=0, st=0, dicc=dicc,
                dics=dics))
    return (render_template('9-states.html', det=0, st=obj, dicc=dicc,
                            dics=dics))


if __name__ == '__main__':
    my_app.run(host='0.0.0.0', port=5000)
