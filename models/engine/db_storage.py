#!/usr/bin/python3
"""This module was created for databasestorage"""

from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import create_engine
from os import environ
from models.base_model import Base, BaseModel
from models.city import City
from models.user import User
from models.state import State
from models.amenity import Amenity
from models.place import Place
from models.review import Review

user = environ['HBNB_MYSQL_USER']
passw = environ['HBNB_MYSQL_PWD']
hos = environ['HBNB_MYSQL_HOST']
dabase = environ['HBNB_MYSQL_DB']


class DBStorage():
    """Implement new storage engine using SQLALCHEMY"""

    __engine = None
    __session = None

    def __init__(self):
        str = "mysql+mysqldb://{}:{}@{}:443/{}".format(user, passw,
                                                       hos, dabase)
        self.__engine = create_engine(str, pool_pre_ping=True)
        if environ.get("HBNB_ENV") == "test":
            Base.metadata.drop_all()

    def all(self, cls=None):
        """Returns dictionary of instances currently in session"""

        dict_obj = {}
        list_res = []
        if cls is None:
            list_res.append(self.__session.query(City))
            list_res.append(self.__session.query(State))
            list_res.append(self.__session.query(User))
            list_res.append(self.__session.query(Amenity))
            list_res.append(self.__session.query(Place))
            list_res.append(self.__session.query(Review))
            for item in list_res:
                for obj in item:
                    str = "{}.{}". format(obj.__class__.__name__, obj.id)
                    dict_obj.update({str: obj})
            print(list_res)
        else:
            print(cls)
            list_res = []
            if (cls == "User" or cls is User):
                list_res = self.__session.query(User)
            if (cls == "Review" or cls is User):
                list_res = self.__session.query(Review)
            if (cls == "State" or cls is State):
                list_res = self.__session.query(State)
            if (cls == "City" or cls is City):
                list_res = self.__session.query(City)
            if (cls == "Amenity" or cls is Amenity):
                list_res = self.__session.query(Amenity)
            if (cls == "Place" or cls is Place):
                list_res = self.__session.query(Place)
            for obj in list_res:
                str = "{}.{}". format(obj.__class__.__name__, obj.id)
                dict_obj.update({str: obj})
        return (dict_obj)

    def new(self, obj):
        """Add object to session"""

        self.__session.add(obj)

    def save(self):
        """Save objects in session to database"""
        self.__session.commit()

    def delete(self, obj=None):
        """Ruthlessly delete an object from the current session"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """Creates objects from table in database"""

        Base.metadata.create_all(self.__engine)
        self.__session = scoped_session(sessionmaker(bind=self.__engine,
                                                     expire_on_commit=False))

    def close(self):
        """End a session"""
        self.__session.remove()
