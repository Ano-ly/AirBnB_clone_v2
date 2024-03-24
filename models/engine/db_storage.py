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

    def all(self, cls=None):
        """Returns dictionary of instances currently in session"""

        my_session = self.__session()
        dict_obj = {}
        if cls is None:
            list_res = []
            list_res.append(my_session.query(City))
            list_res.append(my_session.query(State))
            list_res.append(my_session.query(User))
            list_res.append(my_session.query(Amenity))
            list_res.append(my_session.query(Place))
            list_res.append(my_session.query(Review))
            for item in list_res:
                for obj in item:
                    str = "{}.{}". format(obj.__class__.__name__, obj.id)
                    dict_obj.update({str: obj})
            print(list_res)
        else:
            if (cls == "User"):
                list_res = my_session.query(User)
            if (cls == "Review"):
                list_res = my_session.query(Review)
            if (cls == "State"):
                list_res = my_session.query(State)
            if (cls == "City"):
                list_res = my_session.query(City)
            if (cls == "Amenity"):
                list_res = my_session.query(Amenity)
            if (cls == "Place"):
                list_res = my_session.query(Place)
            for obj in list_res:
                str = "{}.{}". format(obj.__class__.__name__, obj.id)
                dict_obj.update({str: obj})
        my_session.close()
        return (dict_obj)

    def new(self, obj):
        """Add object to session"""

        my_session = self.__session()
        my_session.add(obj)
        my_session.close

    def save(self):
        """Save objects in session to database"""
        my_session = self.__session()
        self.__session.commit()
        my_session.close()

    def delete(self, obj=None):
        """Ruthlessly delete an object from the current session"""
        my_session = self.__session()
        if obj is not None:
            my_session.delete(obj)
        my_session.close()

    def reload(self):
        """Creates objects from table in database"""

        Base.metadata.create_all(self.__engine)
        self.__session = scoped_session(sessionmaker(bind=self.__engine,
                                                     expire_on_commit=False))

    def close(self):
        """End a session"""
        self.__session.remove()
