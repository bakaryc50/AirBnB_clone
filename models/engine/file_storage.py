#!/usr/bin/python3
""" This file provide the module for data storage class """
from models.base_model import BaseModel
import json


class FileStorage:
    """ FileStorage class that serializes instances to a JSON file
    and deserializes JSON file to instances
    Attributes:
    __file_path: string - path to json file
    __objects: dictionary - empty but will store all objects by class name.id
    """
    __file_path = "file.json"
    __objects = dict()

    def all(self, cls=None):
        """ returns the dictionary __objects
        """
        if cls is None:
            return self.__objects.copy()
        else:
            return {
                    key: obj for key, obj in self.__objects.items()
                    if type(obj) is cls
                    }

    def new(self, obj):
        """ register new object
        sets __object to a given obj
        """
        if obj:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
        """ save object
        serializes __objects to the JSON file __file_path
        """
        new_dict = {key: obj.to_dict() for key, obj in self.__objects.items()}
        with open(self.__file_path, "w", encoding="UTF-8") as f:
            json.dump(new_dict, f)

    def delete(self, obj=None):
        """delete obj from __objects
        """
        if isinstance(obj, BaseModel):
            key = "{}.{}".format(type(obj).__name__, obj.id)
            if key in self.__objects:
                del self.__objects[key]

    def reload(self):
        """ load the object from json file
        deserializes the json file to __objects
        """
        try:
            with open(self.__file_path, "r", encoding="UTF-8") as f:
                for key, value in (json.load(f)).items():
                    value = eval(value["__class__"])(**value)
                    self.__objects[key] = value
        except FileNotFoundError:
            pass
