#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from models.city import City
from models.engine.file_storage import FileStorage


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade="all, delete-orphan")

    @property
    def cities(self):
        """getter attribute. returns child states"""
        my_dict = FileStorage.all(City)
        new_dict = {k: v for k, v in my_dict if v.state_id == self.id}
