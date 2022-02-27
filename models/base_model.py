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
                    setattr(self, attr, kwargs[attr])
        else:

#		print("sabes q no habia kwargs? voy al args")
#if len(args) > 3:
#			raise TypeError("You only can set 2 attrs")
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)
#		attrs = {0: 'created_at', 1: 'updated_at'}
#		print("voy a setear los args")
#		for i in range(len(args)):
#			self.attrs[i] = args[i]
#		print("ya setee los args")

    def __str__(self):
        """
        methods which returns an string instance representation
        """
        return f'[{type(self).__name__}] ({self.id}) {self.__dict__}'

    def save(self):
        """
        updates the public instance attribute updated_at with the current datetime
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        returns a dictionary with all keys/values of the instance
        """
        ret = self.__dict__.copy()
        ret['created_at'] = ret['created_at'].isoformat()
        ret['updated_at'] = ret['updated_at'].isoformat()
        return ret
