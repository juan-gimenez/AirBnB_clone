#!/usr/bin/python3
"""
Module base_model.py - contains the base model class
"""


from abc import ABC, abstractmethod
from uuid import uuid4
from datetime import datetime
from models import storage
class BaseModel(ABC):
    """
    Class BaseModel class - defines common attributes/methods for the sublclasses
    """


    def __init__(self, *args, **kwargs):
        """
        method which initializes the instance attributes
        """
        if len(kwargs) != 0:
            for attr in kwargs:
                if attr != "__class__":
                    if attr == "created_at" or attr == "updated_at":
                        setattr(self, attr, strptime(kwargs[attr], '%Y-%m-%dT%H:%M:%S.%f'))
                    else:
                        setattr(self, attr, kwargs[attr])
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

#   @property
#    @abstractmethod
    def __str__(self):
        """
        methods which returns an string instance representation
        """
        print("entre al str del base model")
        return f'[{self.__class__.__name__}] ({self.id}) {self.__dict__}'

 #   @abstractmethod
    def save(self):
        """
        updates the public instance attribute updated_at with the current datetime
        """
        self.updated_at = datetime.now()
        storage.save()

#    @abstractmethod
    def to_dict(self):
        """
        returns a dictionary with all keys/values of the instance
        """
        ret = self.__dict__.copy()
        ret['created_at'] = ret['created_at'].isoformat()
        ret['updated_at'] = ret['updated_at'].isoformat()
        return ret
