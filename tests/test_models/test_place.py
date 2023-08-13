#!/usr/bin/python3
"""Unittest for Place class"""

import unittest
import os
from models.place import Place
from datetime import datetime
from time import sleep
from models.base_model import BaseModel
import uuid


class TestPlace(unittest.TestCase):
    """Tests the Place class model"""

    @classmethod
    def setUpClass(cls):
        """Setup the unittest"""
        cls.place = Place()
        cls.place.city_id = str(uuid.uuid4())
        cls.place.user_id = str(uuid.uuid4())
        cls.place.name = "Any place in the world"
        cls.place.description = "Suny Beatch"
        cls.place.number_rooms = 0
        cls.place.number_bathrooms = 0
        cls.place.max_guest = 0
        cls.place.price_by_night = 0
        cls.place.latitude = 0.0
        cls.place.longitude = 0.0
        cls.place.amenity_ids = []

    @classmethod
    def tearDownClass(cls):
        """Deletes the class"""
        del cls.place
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def testissubclass(self):
        self.assertTrue(issubclass(self.place.__class__, BaseModel))

    def checkingfordoc(self):
        self.assertIsNotNone(Place.__doc__)

    def testhasattributes(self):
        self.assertTrue('id' in self.place.__dict__)
        self.assertTrue('created_at' in self.place.__dict__)
        self.assertTrue('updated_at' in self.place.__dict__)
        self.assertTrue('city_id' in self.place.__dict__)
        self.assertTrue('user_id' in self.place.__dict__)
        self.assertTrue('name' in self.place.__dict__)
        self.assertTrue('max_guest' in self.place.__dict__)
        self.assertTrue('price_by_night' in self.place.__dict__)
        self.assertTrue('latitude' in self.place.__dict__)
        self.assertTrue('longitude' in self.place.__dict__)
        self.assertTrue('amenity_ids' in self.place.__dict__)
        self.assertTrue('description' in self.place.__dict__)
        self.assertTrue('number_rooms' in self.place.__dict__)
        self.assertTrue('number_bathrooms' in self.place.__dict__)

    def testattributesarestring(self):
        self.assertIs(type(self.place.city_id), str)
        self.assertIs(type(self.place.user_id), str)
        self.assertIs(type(self.place.name), str)
        self.assertIs(type(self.place.description), str)
        self.assertIs(type(self.place.number_rooms), int)
        self.assertIs(type(self.place.max_guest), int)
        self.assertIs(type(self.place.price_by_night), int)
        self.assertIs(type(self.place.latitude), float)
        self.assertIs(type(self.place.longitude), float)
        self.assertIs(type(self.place.amenity_ids), list)

    def testsave(self):
        self.place.save()
        self.assertNotEqual(self.place.created_at, self.place.updated_at)

    def testonesave(self):
        namePlace = Place()
        sleep(0.05)
        ONEupdated_at = namePlace.updated_at
        namePlace.save()
        self.assertLess(ONEupdated_at, namePlace.updated_at)

    def testtwosaves(self):
        namePlace = Place()
        sleep(0.05)
        ONEupdated_at = namePlace.updated_at
        namePlace.save()
        TWOupdated_at = namePlace.updated_at
        self.assertLess(ONEupdated_at, TWOupdated_at)
        sleep(0.05)
        namePlace.save()
        self.assertLess(TWOupdated_at, namePlace.updated_at)

    def testsavewitharg(self):
        namePlace = Place()
        with self.assertRaises(TypeError):
            namePlace.save(None)


class TestPlacetodict(unittest.TestCase):
    """Testing Place class dict methods"""

    def testtodicttype(self):
        self.assertTrue(dict, type(Place().to_dict()))

    def testtodictcontainscorrectkeys(self):
        namePlace = Place()
        self.assertIn("id", namePlace.to_dict())
        self.assertIn("created_at", namePlace.to_dict())
        self.assertIn("updated_at", namePlace.to_dict())
        self.assertIn("__class__", namePlace.to_dict())

    def testtodictcontainsaddedattributes(self):
        namePlace = Place()
        namePlace.middle_name = "Surulere"
        namePlace.my_number = 98
        self.assertEqual("Surulere", namePlace.middle_name)
        self.assertIn("my_number", namePlace.to_dict())

    def testtodictdatetimeattributesarestring(self):
        namePlace = Place()
        namePlace_dict = namePlace.to_dict()
        self.assertEqual(str, type(namePlace_dict["id"]))
        self.assertEqual(str, type(namePlace_dict["created_at"]))
        self.assertEqual(str, type(namePlace_dict["updated_at"]))

    def testtodictoutput(self):
        date_time = datetime.today()
        namePlace = Place()
        namePlace.id = "123456"
        namePlace.created_at = namePlace.updated_at = date_time
        dict_output = {
            'id': '123456',
            '__class__': 'Place',
            'created_at': date_time.isoformat(),
            'updated_at': date_time.isoformat(),
        }
        self.assertDictEqual(namePlace.to_dict(), dict_output)

    def testcontrasttodictdunderdict(self):
        namePlace = Place()
        self.assertNotEqual(namePlace.to_dict(), namePlace.__dict__)

    def testtodictwitharg(self):
        namePlace = Place()
        with self.assertRaises(TypeError):
            namePlace.to_dict(None)


if __name__ == "__main__":
    unittest.main()
