#!/usr/bin/python3
""" class FileStorage that serializes instances to a JSON
file and deserializes JSON file to instances"""

import json
from models.base_model import BaseModel
from datetime import datetime


class FileStorage:
    """
    this class will serializes instances
    to a JSON file and deserializes JSON file to instances

    Private class attributes:-

    __file_path: string - path to the JSON file
    __objects:  dictionary - empty but will store all objects by

    Public instance methods:

    all(self): returns the dictionary __objects
    new(self, obj): sets in __objects the obj with key
    save(self): serializes __objects to the JSON file
    reload(self): deserializes the JSON file to __objects
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """method return a dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """method used tot set with the key"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file"""
        obj_to_dict = {key: obj.to_dict()
                       for key, obj in self.__objects.items()}
        with open(self.__file_path, 'w') as file:
            json.dump(obj_to_dict, file)

    def reload(self):
        """
        Deserializes the JSON file to __objects, if the JSON
        file exists, otherwise nothing happens.
        """
        try:
            with open(self.__file_path, 'r') as f:
                data = json.load(f)
                for value in data.values():
                    cls_name = value.get("__class__")
                    if cls_name:
                        cls = eval(cls_name)
                        self.new(cls(**value))
        except Exception:
            pass
