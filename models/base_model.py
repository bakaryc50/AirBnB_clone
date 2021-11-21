#!/usr/bin/python3
""" This file provides the module for BaseModel class implementation """
from uuid import uuid4
from datetime import datetime

import models


class BaseModel:
    """ class for the base model for all models """
    def __init__(self, *args, **kwargs):
        """ BaseModel constructor
        """
        if kwargs:
            for key in kwargs:
                if key in ["created_at", "updated_at"]:
                    setattr(self, key, datetime.fromisoformat(kwargs[key]))
                elif key != "__class__":
                    setattr(self, key, kwargs[key])
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """ Print the string representation of the class
        """
        return "[{}] ({}) {}".format(
                self.__class__.__name__, self.id, self.__dict__
                )

    def save(self):
        """ save the current instance by updating updated_at
        """
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def delete(self):
        """deletes the current instance from the storage
        """
        models.storage.delete(self)

    def to_dict(self):
        """ returns a dictionary containing all keys/values of __dict__ of the instance
        """
        new_dict = self.__dict__.copy()
        new_dict["__class__"] = self.__class__.__name__
        for key in new_dict:
            if key in ["created_at", "updated_at"]:
                new_dict[key] = new_dict[key].isoformat()
        return new_dict
