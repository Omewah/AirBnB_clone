#!/usr/bin/python3
"""Unittest for user class"""

import unittest
import os
from models import storage
from models.user import User
from models.base_model import BaseModel
from datetime import datetime
from time import sleep
import uuid


class TestUserinstantiation(unittest.TestCase):
    """Tests for instantiation"""

    @classmethod
    def setUpClass(cls):
        """Setup the unittest"""
        cls.user = User()
        cls.user.email = "me@example.com"
        cls.user.password = "123i123"
        cls.user.first_name = "John"
        cls.user.last_name = "Swag"

    def testforinstantiation(self):
        """User class instantiation test."""
        user = User()
        self.assertEqual(str(type(user)), "<class 'models.user.User'>")
        self.assertIsInstance(user, User)
        self.assertTrue(issubclass(type(user), BaseModel))

    def testnoargs_instantiates(self):
        self.assertEqual(User, type(User()))

    def testnewinstancestoredinobjects(self):
        self.assertIn(User(), storage.all().values())

    def testidispublic_str(self):
        self.assertEqual(str, type(User().id))

    def testcreated_atispublicdatetime(self):
        self.assertEqual(datetime, type(User().created_at))

    def testhasattributes(self):
        self.assertTrue('id' in self.user.__dict__)
        self.assertTrue('created_at' in self.user.__dict__)
        self.assertTrue('updated_at' in self.user.__dict__)
        self.assertTrue('email' in self.user.__dict__)
        self.assertTrue('password' in self.user.__dict__)
        self.assertTrue('first_name' in self.user.__dict__)
        self.assertTrue('last_name' in self.user.__dict__)

    def testattributesarestring(self):
        self.assertIs(type(self.user.email), str)
        self.assertIs(type(self.user.password), str)
        self.assertIs(type(self.user.first_name), str)
        self.assertIs(type(self.user.last_name), str)

    def testissubclass(self):
        """checks if the User is a subclass of BaseModel"""
        user = User()
        self.assertIsInstance(user, BaseModel)
        self.assertTrue(hasattr(user, "id"))
        self.assertTrue(hasattr(user, "created_at"))
        self.assertTrue(hasattr(user, "updated_at"))

    def testemail_attr(self):
        """Checks the users email attribute"""
        user = User()
        self.assertTrue(hasattr(user, "email"))
        self.assertEqual(user.email, "")

    def testpassword_attr(self):
        """Checks the users password attribute"""
        user = User()
        self.assertTrue(hasattr(user, "password"))
        self.assertEqual(user.password, "")

    def testfirstname_attr(self):
        """Checks the users first name attribute"""
        user = User()
        self.assertTrue(hasattr(user, "first_name"))
        self.assertEqual(user.first_name, "")

    def testlastname_attr(self):
        """Checks the users last name attribute"""
        user = User()
        self.assertTrue(hasattr(user, "last_name"))
        self.assertEqual(user.last_name, "")

    def teststring(self):
        """Checks if the output string method returns correct"""
        user = User()
        string = "[User] ({}) {}".format(user.id, user.__dict__)
        self.assertEqual(string, str(user))

    def testissubclass(self):
        self.assertTrue(issubclass(self.user.__class__, BaseModel))

    def checkingfordoc(self):
        self.assertIsNotNone(User.__doc__)

    def testsave(self):
        self.user.save()
        self.assertNotEqual(self.user.created_at, self.user.updated_at)

    def testtodict(self):
        self.assertTrue('to_dict' in dir(self.user))

    def testtodictcreatesdict(self):
        """Checks if dict is created with the right attributes"""
        user = User()
        user_dict = user.to_dict()
        self.assertEqual(type(user_dict), dict)
        for attr in user.__dict__:
            self.assertTrue(attr in user_dict)
            self.assertTrue("__class__" in user_dict)

    def testtodictvalues(self):
        """test that values in dict returned from to_dict are correct"""
        time_stmp = "%Y-%m-%dT%H:%M:%S.%f"
        user = User()
        user_dict = user.to_dict()
        self.assertEqual(user_dict["__class__"], "User")
        self.assertEqual(type(user_dict["created_at"]), str)
        self.assertEqual(type(user_dict["updated_at"]), str)
        self.assertEqual
        (user_dict["created_at"], user.created_at.strftime(time_stmp))
        self.assertEqual
        (user_dict["updated_at"], user.updated_at.strftime(time_stmp))


if __name__ == "__main__":
    unittest.main()
