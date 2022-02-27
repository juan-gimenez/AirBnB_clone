#!/usr/bin/python3
"""
file_storge module
serializes instances to a JSON file and deserializes JSON file to instance
"""
import json as js
from uuid import uuid4


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
        self.__objects[f'{type(obj).__name__}.{obj.id}'] = obj.to_dict()

    def save(self):
        """
        serializes __objects to the JSON file appending
        """
        try:
            with open (self.__file_path, 'w+') as f:
                f.write(js.dump(self.__objects, f))
        except Exception:
            return

    def reload(self):
        """
       deserializes the JSON file to __objects
        """
        try:
            with open(self.__file_path) as f:
                self.__objects = js.load(f)
                return self.__objects
        except Exception:
            return
