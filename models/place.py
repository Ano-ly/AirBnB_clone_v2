#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from models.review import Review
from models.engine.file_storage import FileStorage
from models.amenity import Amenity
from sqlalchemy import Column, String, Float, Table, ForeignKey, Integer
from sqlalchemy.orm import relationship
from os import environ

place_amenity = Table('place_amenity',
                      Base.metadata,
                      Column('place_id', ForeignKey("places.id"),
                             primary_key=True,
                             nullable=False),
                      Column('amenity_id', ForeignKey("amenities.id"),
                             primary_key=True,
                             nullable=False))


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathroom = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    reviews = relationship("Review", cascade="all, delete-orphan")
    amenity_ids = []

    @property
    def reviews(self):
        """getter attribute. returns child places"""
        my_list = []
        my_dict = FileStorage.all(Review)
        new_dict = {k: v for k, v in my_dict if v.place_id == self.id}
        for item in new_dict.values():
            my_list.append(item)
        return (my_list)

    amenities = relationship("Amenity", secondary=place_amenity,
                             viewonly=False, backref="amenities")

    @property
    def amenities(self):
        """getter attribute. returns amenity places"""
        my_list = []
        my_dict = FileStorage.all(Amenity)
        new_dict = {k: v for k, v in my_dict if v.id in self.amenity_ids}
        for item in new_dict.values():
            my_list.append(item)
        return (my_list)

        @amenities.setter
        def append(self, amenityy):
            """setter attribute, adds amenity to amenity_ids list"""
            if type(amenityy) is Amenity:
                self.amenity_ids.append(amenityy.id)
