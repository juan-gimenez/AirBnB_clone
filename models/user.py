#!/usr/bin/env python3
"""
User module that contains the user class

"""

from models.base_model  import BaseModel
from datetime import datetime
from models import storage
from abc import ABC, abstractmethod

class User(BaseModel):
    """
    User module which manages the users of the system
    """
    
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """ 
        init
        """
        super().__init__(*args, **kwargs)

    @property      
    def __str__(self):
    #""" 
    #str representation of the class user
    #"""
        print("entre al str del user")
        print(f'esto es el return\n**************************\n[{type(self).__name__}] ({self.id}) {self.__dict__}\n*******************************')
        return f'[{type(self).__name__}] ({self.id}) {self.__dict__}'

    def save(self):
        """
        updates the public instance attribute updated_at with the current datetime
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
    #"""
    #returns a dictionary with all keys/values of the instance
    #"""
        ret = self.__dict__.copy()
        print("******************************************")
        for key in ret:
            print(f'bueno vos sabes q soy key: {key}\n value: {ret[key]}\n')
        print("******************************************")
        return ret    
