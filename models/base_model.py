#!/usr/bin/python3
"""
Module base_model.py - contains the base model class
"""


from uuid import uuid4
from datetime import datetime
import models


class BaseModel():
    """
    Class BaseModel class
    - defines common attributes/methods for the sublclasses
    """

    def __init__(self, *args, **kwargs):
        """
        method which initializes the instance attributes
        """
        if len(kwargs) != 0:
            for attr in kwargs:
                if attr != "__class__":
                    if attr == "created_at" or attr == "updated_at":
                        setattr(self, attr, datetime.strptime
                                (kwargs[attr], '%Y-%m-%dT%H:%M:%S.%f'))
                    else:
                        setattr(self, attr, kwargs[attr])
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """
        methods which returns an string instance representation
        """
        return f'[{self.__class__.__name__}] ({self.id}) {self.__dict__}'

    def save(self):
        """
        updates the public instance attribute
        updated_at with the current datetime
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        returns a dictionary with all keys/values of the instance
        """
        ret = self.__dict__.copy()
        ret['__class__'] = type(self).__name__
        ret['created_at'] = ret['created_at'].isoformat()
        ret['updated_at'] = ret['updated_at'].isoformat()
        return ret
