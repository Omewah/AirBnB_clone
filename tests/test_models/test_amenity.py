#!/usr/bin/python3
"""Unittest for the Amenity Class"""

import unittest
import os
from models.amenity import Amenity
from models.base_model import BaseModel
import uuid
import datetime
import time
import re
import json
from models.engine.file_storage import FileStorage
from models import storage


class TestAmenity(unittest.TestCase):
    """Test the Amenity class model"""

    @classmethod
    def setUpClass(cls):
        """Setting up the unittest"""
        cls.amenity = Amenity()
        cls.amenity.name = "Wifi"

    @classmethod
    def tearDownClass(cls):
        """Deletes the class"""
        del cls.amenity
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def testissubclass(self):
        self.assertTrue(issubclass(self.amenity.__class__, BaseModel))

    def checkingfordoc(self):
        self.assertIsNotNone(Amenity.__doc__)

    arm = Amenity()

    def testhasattributes(self):
        """Check for existing attributes"""
        self.assertTrue(hasattr(self.arm, 'name'))
        self.assertTrue(hasattr(self.arm, 'id'))
        self.assertTrue(hasattr(self.arm, 'created_at'))
        self.assertTrue(hasattr(self.arm, 'updated_at'))

    def testattributesarestring(self):
        self.assertIs(type(self.amenity.name), str)

    def testclassexists(self):
        """Checks for existence of a class"""
        cls_exist = "<class 'models.amenity.Amenity'>"
        self.assertEqual(str(type(self.arm)), cls_exist)

    def testuserinheritance(self):
        """Confirms Amenity is a subclass of BaseModel"""
        self.assertIsInstance(self.arm, Amenity)

    def testtypes(self):
        """Confirms the correct type of attributes"""
        self.assertIsInstance(self.arm.name, str)
        self.assertIsInstance(self.arm.id, str)
        self.assertIsInstance(self.arm.created_at, datetime.datetime)
        self.assertIsInstance(self.arm.updated_at, datetime.datetime)

    def testsave(self):
        self.amenity.save()
        self.assertNotEqual(self.amenity.created_at, self.amenity.updated_at)

    def testtodict(self):
        self.assertTrue('to_dict' in dir(self.amenity))


if __name__ == "__main__":
    unittest.main()
