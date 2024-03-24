#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from models.city import City
from models.engine.file_storage import FileStorage
from os import environ


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)

    if environ["HBNB_TYPE_STORAGE"] == "db":
        cities = relationship("City", cascade="all, delete-orphan")
    else:
        @property
        def cities(self):
            from models import storage
            """getter attribute. returns child states"""
            my_dict = models.storage.all()
            new_dict = {k: v for k, v in my_dict.items() if "City" in k}
            new_dict2 = {k: v for k, v in new_dict.items()
                         if v.state_id == self.id}
            return (new_dict2)
