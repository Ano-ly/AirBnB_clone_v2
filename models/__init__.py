#!/usr/bin/python3
"""This module instantiates an object of class FileStorage
or DBStorage, dependng on the value of an environmental variable"""
from os import environ

eng_type = environ.get('HBNB_TYPE_STORAGE')

if eng_type == "db":
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
storage.reload()
