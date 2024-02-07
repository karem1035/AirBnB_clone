#!/usr/bin/python3
import json


class FileStorage:
    __file_path = './file.json'
    __objects = {}

    def all(self):
        """returns a copy of the objects"""
        return self.__objects.copy()

    def new(self, obj):
        """stores the obj in the dictionary using its class name and ID"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """Serializes the objects dictionary to the JSON file."""
        try:
            with open(self.__file_path, 'w') as file:
                json.dumps(self.__objects)
        except:
            pass
            
    def reload(self):
        """Deserializes the objects dictionary to the JSON file."""
    try:
        with open(__file_path, 'r') as file:
            __objects = json.load(file)
    except FileNotFoundError:
            pass
            