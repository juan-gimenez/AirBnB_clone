#!/usr/bin/python3
"""
file_storge module
serializes instances to a JSON file and deserializes JSON file to instance
"""
import json as js
from uuid import uuid4
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

class FileStorage():
    """
    class to manage the serializing and the deserializing JSON's to instances
    """
    __file_path = "file.json"
    __objects = {}


    def all(self):
        """
        returns a dictionary __object
        """


        return self.__objects

    def new(self, obj):
        """
        new(self, obj): sets in __objects the obj with key <obj class name>.id
        """
        self.__objects[f'{type(obj).__name__}.{obj.id}'] = obj

    def save(self):
        """
        serializes __objects to the JSON file appending
        """
        auxDict = {}
        try:
            with open (self.__file_path, 'w+') as f:
                for key, value in self.__objects.items():
                    auxDict[key] = value.to_dict()
                js.dump(auxDict, f)
        except Exception:
            return

    def reload(self):
        """
        deserializes the JSON file to __objects
        """
        try:
            with open(self.__file_path) as f:
                auxDict = js.load(f)
                for key , value in auxDict.items():
                    objAndIdList = str(key).split('.')
                    self.__objects[key] = eval(objAndIdList[0])(**value)
        except Exception:
            return
