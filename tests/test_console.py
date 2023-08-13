#!/usr/bin/python3
"""Unittests for console"""
import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class TestHBNBCommand(unittest.TestCase):
    """Unittests for console and subsystem commands"""
    def setUp(self):
        self.console = HBNBCommand()

    def tearDown(self):
        pass

    def testquitcommand(self):
        with patch('sys.stdout', new=StringIO()) as str:
            self.assertTrue(self.console.quit_cls(''))
            self.assertEqual(str.getvalue().strip(), "Thanks and Good-Bye!")

    def testblankcommand(self):
        self.assertFalse(self.console.blank_cmd())

    def testviewinstcommand(self):
        with patch('sys.stdout', new=StringIO()) as str:
            self.console.view_inst('')
            self.assertTrue("class name missing **" in str.getvalue())
            str.truncate(0)

        with patch('sys.stdout', new=StringIO()) as str:
            self.console.view_inst('InvalidClass')
            self.assertTrue("class doesn't exist **" in str.getvalue())
            str.truncate(0)

        with patch('sys.stdout', new=StringIO()) as str:
            self.console.view_inst('BaseModel')
            self.assertTrue("instance id missing **" in str.getvalue())
            str.truncate(0)

if __name__ == "__main__":
    unittest.main()
