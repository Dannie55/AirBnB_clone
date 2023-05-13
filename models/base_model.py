#!/usr/bin/python3
"""Defines the BaseModel Class"""
import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """Represent a class from which other classes inherits"""

    def __init__(self, *args, **kwargs):

        """initializes a new BaseModel,

        Args:
            *args (any): Unused.
            **kwargs (dict) : key/value pairs of attributes
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                elif key == 'updated_at':
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                elif key == 'created_at':
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if 'id' not in kwargs.keys():
                    self.id = str(uuid4())
                if 'created_at' not in kwargs.keys():
                    self.created_at = datetime.now()
                if 'updated_at' not in kwargs.keys():
                    self.updated_at = datetime.now()
                setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)

    def __str__(self):
        """String"""
        return('[' + type(self).__name__ + '] (' + str(self.id) +
               ') ' + str(self.__dict__))

    def save(self):
        """save function"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Return a dictionary"""
        my_dict = self.__dict__.copy()
        my_dict['__class__'] = self.__class__.__name__
        my_dict['created_at'] = self.created_at.isoformat()
        my_dict['updated_at'] = self.updated_at.isoformat()
        return my_dict
