#!/usr/bin/python3
""" test module for user class """
import unittest
import os
from models.user import User
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """ This will test the User class
    """
    @classmethod
    def setUpClass(cls):
        """ set up for test
        """
        cls.user = User()
        cls.user.first_name = "Bakary"
        cls.user.last_name = "CAMARA"
        cls.user.email = "bakaryc50@gmamil.com"
        cls.user.password = "mdp"

    @classmethod
    def teardown(cls):
        """after the test it will tear it down
        """
        del cls.user

    def tearDown(self):
        """tear it Down
        """
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_check_for_docstring_User(self):
        """" checks for docstring
        """
        self.assertIsNotNone(User.__doc__)

    def test_attributes_User(self):
        """it checks if User has attribute
        """
        self.assertTrue("email" in self.user.__dict__)
        self.assertTrue("id" in self.user.__dict__)
        self.assertTrue('created_at' in self.user.__dict__)
        self.assertTrue('updated_at' in self.user.__dict__)
        self.assertTrue('password' in self.user.__dict__)
        self.assertTrue('first_name' in self.user.__dict__)
        self.assertTrue('last_name' in self.user.__dict__)

    def test_is_subclass_User(self):
        """ tests if User is subclass of BaseModel
        """
        self.assertTrue(issubclass(self.user.__class__, BaseModel), True)

    def test_attribute_types_User(self):
        """ tests the attribute type for User
        """
        self.assertEqual(type(self.user.email),  str)
        self.assertEqual(type(self.user.password), str)
        self.assertEqual(type(self.user.first_name), str)
        self.assertEqual(type(self.user.last_name), str)

    def test_save_User(self):
        """test if the save works"""
        self.user.save()
        self.assertNotEqual(self.user.created_at, self.user.updated_at)

    def test_to_dict_User(self):
        """test if dictionary works"""
        self.assertEqual('to_dict' in dir(self.user), True)
