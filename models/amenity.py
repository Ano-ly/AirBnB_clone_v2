#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Table


class Amenity(BaseModel, Base):
    """Amenity class"""

    __tablename__ = "amenities"
    name = Column(String(128), nullable=False)
    place_amenity = Table('association',
                          Base.metadata,
                          Column('place_id', ForeignKey("places.id"),
                                 nullable=False),
                          Column('amenity_id', ForeignKey("amenities.id"),
                                 nullable=False))
