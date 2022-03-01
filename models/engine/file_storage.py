#!/usr/bin/python3
"""
file_storge module
serializes instances to a JSON file and deserializes JSON file to instance
"""
import json as js
from uuid import uuid4
from models.base_model import BaseModel

class FileStorage():
    """
    class to manage the serializing and the deserializing JSON's to instances
    """
    __file_path = "file.json"
    __objects = {}


    def all(self):
        """
        returns an empty dictionary __object
        """


        return self.__objects

    def new(self, obj):
        """
        new(self, obj): sets in __objects the obj with key <obj class name>.id
        """
        self.__objects[f'{type(obj).__name__}.{obj.id}'] = obj
        print(f'este es el self.__objects: \n{self.__objects}')

    def save(self):
        """
        serializes __objects to the JSON file appending
        """
        auxDict = {}
        try:
            with open (self.__file_path, 'w+') as f:
                for key, value in self.__objects.items():
                    auxDict[key] = value.to_dict()
                f.write(js.dumps(auxDict))
        except Exception as a:
            print("except del open la concha de tu madre")
            print(a)
            raise a
            return

    def reload(self):
        """
        deserializes the JSON file to __objects
        """
        try:
            with open(self.__file_path) as f:
                auxDict = js.load(f)
                for key in auxDict:
                    self.__objects[key] = Basemodel(**auxDict[key])
                    
                return self.__objects
        except Exception:
            return
