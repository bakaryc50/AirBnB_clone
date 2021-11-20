#!/usr/bin/python3
""" Provides the unittest for BaseModel class """
from models.base_model import BaseModel
import unittest
from datetime import datetime
from uuid import UUID, uuid4
from time import sleep


class TestBaseModel(unittest.TestCase):
    """ tests the BaseModel class
    """
    def test(self):
        """ task test for public instance attributes
        """
        my_model = BaseModel()

        # id: format and uniqueness
        self.assertTrue(
                type(getattr(my_model, "id", None) is str) and
                UUID(my_model.id)
                )
        self.assertNotEqual(BaseModel().id, my_model.id)
        self.assertNotEqual(BaseModel().id, BaseModel().id)

        # created_at and updated_at types
        self.assertTrue(type(my_model.created_at) is datetime)
        self.assertTrue(type(my_model.updated_at) is datetime)

        # string representation
        self.assertEqual(str(my_model), "[{}] ({}) {}".format(
            "BaseModel", my_model.id, my_model.__dict__))

        # time updates
        old_crtm = my_model.created_at
        old_uptm = my_model.updated_at
        sleep(0.01)
        my_model.save()

        self.assertEqual(old_crtm, my_model.created_at)
        self.assertNotEqual(old_uptm, my_model.updated_at)

        self.assertEqual(my_model.to_dict(), {
            "__class__": "BaseModel",
            "id": my_model.id,
            "created_at": my_model.created_at.isoformat(),
            "updated_at": my_model.updated_at.isoformat()

            })
