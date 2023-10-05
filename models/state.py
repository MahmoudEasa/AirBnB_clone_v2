#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import models
from models.city import City
from os import getenv


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade="delete", backref="state")

    if getenv("HBNB_TYPE_STORAGE") != 'db':
        @property
        def cities(self):
            """ getter attribute cities that returns the list of City """
            city_list = []
            for city in list(models.storage.all(City).values()):
                if city.state.id == self.id:
                    city_list.append(city)
            return city_list
