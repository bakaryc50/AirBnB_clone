#!/usr/bin/python3
""" This file provide the unit test module for the console """
import unittest
import json
import os
from io import StringIO
from unittest.mock import patch
import tests
import console

from console import HBNBCommand
from models import storage
from models.base_model import BaseModel


class TestHBNBCommand(unittest.TestCase):
    """ The test class for HBNBCommand class
    """
    @classmethod
    def setUpClass(cls):
        """ setup for the test
        """
        cls.consol = HBNBCommand()

    @classmethod
    def teardown(cls):
        """ at the end of the test, it will tear it down
        """
        del cls.consol

    def tearDown(self):
        """ it will remove temp file (file.json) created as a result
        """
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_docstrings_in_console(self):
        """ checks for docstrings
        """
        self.assertIsNotNone(console.__doc__)
        self.assertIsNotNone(HBNBCommand.emptyline.__doc__)
        self.assertIsNotNone(HBNBCommand.do_quit.__doc__)
        self.assertIsNotNone(HBNBCommand.do_EOF.__doc__)

    def test_emptyline(self):
        """ tests empty line input
        """
        with patch("sys.stdout", new=StringIO()) as f:
            self.consol.onecmd("\n")
            self.assertEqual(f.getvalue(), "")

    def test_quit(self):
        """ tests quit command
        """
        with patch("sys.stdout", new=StringIO()) as f:
            self.consol.onecmd("quit")
            self.assertEqual(f.getvalue(), "")

    def test_create(self):
        """ tests the create command
        """
        with patch("sys.stdout", new=StringIO()) as f:
            self.consol.onecmd("create")
            self.assertEqual(f.getvalue(), "** class name missing **\n")
        with patch("sys.stdout", new=StringIO()) as f:
            self.consol.onecmd("create MyModel")
            self.assertEqual(f.getvalue(), "** class doesn't exist **\n")

    def test_show(self):
        """ tests the show command
        """
        with patch("sys.stdout", new=StringIO()) as f:
            self.consol.onecmd("show")
            self.assertEqual(f.getvalue(), "** class name missing **\n")
        with patch("sys.stdout", new=StringIO()) as f:
            self.consol.onecmd("show MyModel")
            self.assertEqual(f.getvalue(), "** class doesn't exist **\n")

    def test_destroy(self):
        """Test destroy command inpout"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("destroy")
            self.assertEqual(
                "** class name missing **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("destroy MyModel")
            self.assertEqual(
                "** class doesn't exist **\n", f.getvalue())

    def test_all(self):
        """ tests the print of all string representation of
        an instance
        """
        with patch("sys.stdout", new=StringIO()) as f:
            self.consol.onecmd("all MyModel")
            self.assertEqual(f.getvalue(), "** class doesn't exist **\n")
        with patch("sys.stdout", new=StringIO()) as f:
            self.consol.onecmd("all BaseModel")
            self.assertEqual(f.getvalue(), "[]\n")
