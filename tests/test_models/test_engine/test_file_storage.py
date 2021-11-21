#!/usr/bin/python3
""" This file provide the unittest case for FileStorage class """
import unittest
import json
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage

import os


class TestFileStorage(unittest.TestCase):
    """ Tests the FileStorage functions
    """
    def test_all(self):
        """ tests if all works in FileStorage
        """
        storage = FileStorage()
        obj = storage.all()
        self.assertIsNotNone(obj)
        self.assertEqual(type(obj), dict)
        self.assertIs(obj, storage._FileStorage__objects)

    def test_new(self):
        """ tests when new is created
        """
        storage = FileSotrage()
        obj = storage.all()
        my_model = BaseModel()
        storage.new(my_model)
        key = my_model.__class__.__name__ + "." + str(my_model.id)
        self.assertIsNotNone(obj[key])
