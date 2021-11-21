#!/usr/bin/python3
""" test module for state class """
import unittest
import os
from models.state import State
from models.base_model import BaseModel


class TestState(unittest.TestCase):
    """ This will test the State class
    """
    @classmethod
    def setUpClass(cls):
        """ set up for test
        """
        cls.state = State()
        cls.state.name = "state name"

    @classmethod
    def teardown(cls):
        """after the test it will tear it down
        """
        del cls.state

    def tearDown(self):
        """tear it Down
        """
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_check_for_docstring_State(self):
        """" checks for docstring
        """
        self.assertIsNotNone(State.__doc__)

    def test_attributes_State(self):
        """it checks if State has attribute
        """
        self.assertTrue("name" in self.state.__dict__)
        self.assertTrue("id" in self.state.__dict__)
        self.assertTrue("created_at" in self.state.__dict__)
        self.assertTrue("updated_at" in self.state.__dict__)

    def test_is_subclass_State(self):
        """ tests if State is subclass of BaseModel
        """
        self.assertTrue(issubclass(self.state.__class__, BaseModel), True)

    def test_attribute_types_State(self):
        """ tests the attribute type for State
        """
        self.assertEqual(type(self.state.name),  str)

    def test_save_State(self):
        """test if the save works"""
        self.state.save()
        self.assertNotEqual(self.state.created_at, self.state.updated_at)

    def test_to_dict_State(self):
        """test if dictionary works"""
        self.assertEqual('to_dict' in dir(self.state), True)
