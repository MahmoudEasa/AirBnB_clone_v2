#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from models.amenity import Amenity
from models.review import Review
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
import os
import models

place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id', String(60),
                             ForeignKey('places.id'),
                             primary_key=True, nullable=False),
                      Column('amenity_id', String(60),
                             ForeignKey('amenities.id'),
                             primary_key=True, nullable=False))


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"

    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(60), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []

    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        amenities = relationship("Amenity", secondary=place_amenity,
                                 viewonly=False)
        reviews = relationship("Review", cascade="all, delete",
                               backref="place")

    else:
        @property
        def amenities(self):
            """Getter attribute amenities"""
            amenity_objs = []
            for amenity_id in self.amenity_ids:
                amenity_obj = models.storage.get("Amenity", amenity_id)
                if amenity_obj:
                    amenity_objs.append(amenity_obj)
            return amenity_objs

        @amenities.setter
        def amenities(self, obj):
            """Setter attribute amenities"""
            if isinstance(obj, Amenity):
                self.amenity_ids.append(obj.id)

        @property
        def reviews(self):
            """Getter attribute reviews"""
            review_objs = []
            for review in models.storage.all("Review").values():
                if review.place_id == self.id:
                    review_objs.append(review)
            return review_objs
