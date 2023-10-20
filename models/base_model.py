#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
import models
from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


class BaseModel:
    """Attributes:
        id: unique string (60 characters), can't be null, primary key
        created_at: datetime, can't be null, default value is datetime.utcnow()
        updated_at: datetime, can't be null, default value is datetime.utcnow()
    """
    id = Column(String(60), nullable=False, primary_key=True)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())

    """A base class for all hbnb models"""
    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        else:
            try:
                kwargs['updated_at'] =\
                        datetime.strptime(kwargs['updated_at'],
                                          '%Y-%m-%dT%H:%M:%S.%f')
                kwargs['created_at'] =\
                    datetime.strptime(kwargs['created_at'],
                                      '%Y-%m-%dT%H:%M:%S.%f')
            except KeyError:
                self.updated_at = datetime.now()
                self.created_at = datetime.now()
                pass

            if 'id' not in kwargs:
                self.id = str(uuid.uuid4())

            kwargs.pop('__class__', None)
            self.__dict__.update(kwargs)

            # Update instance attributes from kwargs
            for key, value in kwargs.items():
                if not hasattr(self, key):
                    setattr(self, key, value)

    def __str__(self):
        """Return the print/str representation of the BaseModel instance."""
        d = self.__dict__.copy()
        d.pop("_sa_instance_state", None)
        return "[{}] ({}) {}".format(type(self).__name__, self.id, d)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = {}
        dictionary.update(self.__dict__)
        dictionary.update({'__class__':
                          (str(type(self)).split('.')[-1]).split('\'')[0]})
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        if '_sa_instance_state' in dictionary:
            del dictionary['_sa_instance_state']
        return dictionary

    def delete(self):
        """Delete the current instance from the storage"""
        models.storage.delete(self)
