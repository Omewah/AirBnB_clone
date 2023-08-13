#!/usr/bin/python3
"""Unittest for City Class"""

import unittest
from datetime import datetime
import time
import uuid
from models.city import City
import re
import json
from models.engine.file_storage import FileStorage
import os
from models import storage
from models.base_model import BaseModel

class TestCity(unittest.TestCase):
    """Tests the City class model"""

    @classmethod
    def setUpClass(cls):
        """Setup the unittest"""
        cls.city = City()
        cls.city.state_id = str(uuid.uuid4())
        cls.city.name = "Lagos, Nigeria"

    @classmethod
    def tearDownClass(cls):
        """Deletes the class"""
        del cls.city
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def testnoargsinstantiates(self):
        self.assertEqual(City, type(City()))

    def testnewinstancestoredinobjects(self):
        self.assertIn(City(), storage.all().values())

    def testidispublicstr(self):
        self.assertEqual(str, type(City().id))

    def testcreatedatispublicdatetime(self):
        self.assertEqual(datetime, type(City().created_at))

    def testupdatedatispublicdatetime(self):
        self.assertEqual(datetime, type(City().updated_at))

    def testissubclass(self):
        self.assertTrue(issubclass(self.city.__class__, BaseModel))

    def checkingfordoc(self):
        self.assertIsNotNone(City.__doc__)

    def testhasattributes(self):
        self.assertTrue('id' in self.city.__dict__)
        self.assertTrue('created_at' in self.city.__dict__)
        self.assertTrue('updated_at' in self.city.__dict__)
        self.assertTrue('state_id' in self.city.__dict__)
        self.assertTrue('name' in self.city.__dict__)

    def teststateidispublicclassattribute(self):
        nameCity = City()
        self.assertEqual(str, type(City.state_id))
        self.assertIn("state_id", dir(nameCity))
        self.assertNotIn("state_id", nameCity.__dict__)

    def testnameispublicclassattribute(self):
        nameCity = City()
        self.assertEqual(str, type(City.name))
        self.assertIn("name", dir(nameCity))
        self.assertNotIn("name", nameCity.__dict__)

    def testattributesarestring(self):
        self.assertIs(type(self.city.state_id), str)
        self.assertIs(type(self.city.name), str)

    def testsave(self):
        self.city.save()
        self.assertNotEqual(self.city.created_at, self.city.updated_at)

    def testtodict(self):
        self.assertTrue('to_dict' in dir(self.city))


if __name__ == "__main__":
    unittest.main()
