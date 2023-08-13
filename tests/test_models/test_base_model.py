#!/usr/bin/python3
"""Unittest for base models"""
from fileinput import lineno
import unittest
from models import storage
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from datetime import datetime
from time import sleep
import time
import uuid
import json
import os
import re


class TestBaseModelInstantiation(unittest.TestCase):
    """Unittests for testing instantiation"""

    def testIsInstanceOf(self):
        """Test IsInstance"""
        bm1 = BaseModel()
        self.assertIsInstance(bm1, BaseModel)
        self.assertEqual
        (str(type(bm1)), "<class 'models.base_model.BaseModel'>")
        self.assertTrue(issubclass(type(bm1), BaseModel))

    def testContainsId(self):
        """Tests if ID is valid"""
        bm1 = BaseModel()
        self.assertTrue(hasattr(bm1, "id"))

    def testIdType(self):
        """Test the ID type of  the model"""
        bm1 = BaseModel()
        self.assertEqual(type(bm1.id), str)

    def testCompareTwoInstancesId(self):
        """Compares two instances ID"""
        bm1 = BaseModel()
        bm2 = BaseModel()
        self.assertNotEqual(bm1.id, bm2.id)

    def testuuid(self):
        """Test for valid user id"""
        bm1 = BaseModel()
        bm2 = BaseModel()
        for inst in [bm1, bm2]:
            uuid = inst.id
            with self.subTest(uuid=uuid):
                self.assertIs(type(uuid), str)
                self.assertRegex(uuid,
                                 '^[0-9a-f]{8}-[0-9a-f]{4}'
                                 '-[0-9a-f]{4}-[0-9a-f]{4}'
                                 '-[0-9a-f]{12}$')
        self.assertNotEqual(bm1.id, bm2.id)

    def testuniq_id(self):
        """checks for unique user IDs."""
        uq = [BaseModel().id for i in range(1000)]
        self.assertEqual(len(set(uq)), len(uq))

    def testtwomodelsuniqueid(self):
        bm1 = BaseModel()
        bm2 = BaseModel()
        self.assertNotEqual(bm1.id, bm2.id)

    def testnewinstancestoredinobjects(self):
        self.assertIn(BaseModel(), storage.all().values())

    def testContainsCreated_at(self):
        """Tests created_at attribute"""
        bm1 = BaseModel()
        self.assertTrue(hasattr(bm1, "created_at"))

    def testCreated_atInstance(self):
        """Tests created_at attribute instances"""
        bm1 = BaseModel()
        self.assertIsInstance(bm1.created_at, datetime)

    def testContainsUpdated_at(self):
        """Tests updated_at attributes"""
        bm1 = BaseModel()
        self.assertTrue(hasattr(bm1, "updated_at"))

    def testUpdated_atInstance(self):
        """Tests updated_at attribute instance"""
        bm1 = BaseModel()
        self.assertIsInstance(bm1.updated_at, datetime)

    def testdatetimecreated(self):
        """Tests updated_at + created_at current status"""
        current_dt = datetime.now()
        bm1 = BaseModel()
        compare_bm = bm1.updated_at - bm1.created_at
        self.assertTrue(abs(compare_bm.total_seconds()) < 0.01)
        compare_bm = bm1.created_at - current_dt
        self.assertTrue(abs(compare_bm.total_seconds()) < 0.1)

    def testidispublicstr(self):
        self.assertEqual(str, type(BaseModel().id))

    def testcreated_atispublicdatetime(self):
        self.assertEqual(datetime, type(BaseModel().created_at))

    def testupdated_atispublicdatetime(self):
        self.assertEqual(datetime, type(BaseModel().updated_at))

    def teststringrepr(self):
        date_time = datetime.today()
        time_stmp = repr(date_time)
        bm1 = BaseModel()
        bm1.id = "123456"
        bm1.created_at = bm1.updated_at = date_time
        bm1str = bm1.__str__()
        self.assertIn("[BaseModel] (123456)", bm1str)
        self.assertIn("'id': '123456'", bm1str)
        self.assertIn("'created_at': " + time_stmp, bm1str)
        self.assertIn("'updated_at': " + time_stmp, bm1str)

    def testargsunused(self):
        bm1 = BaseModel(None)
        self.assertNotIn(None, bm1.__dict__.values())

    def testinstantiationwithkwargs(self):
        date_time = datetime.today()
        date_time_iso = date_time.isoformat()
        bm1 = BaseModel
        (id="345", created_at=date_time_iso, updated_at=date_time_iso)
        self.assertEqual(bm1.id, "345")
        self.assertEqual(bm1.created_at, date_time)
        self.assertEqual(bm1.updated_at, date_time)

    def testinstantiationwithNonekwargs(self):
        with self.assertRaises(TypeError):
            BaseModel(id=None, created_at=None, updated_at=None)

    def testinstantiationwithargsandkwargs(self):
        date_time = datetime.today()
        date_time_iso = date_time.isoformat()
        bm1 = BaseModel
        ("12", id="345", created_at=date_time_iso, updated_at=date_time_iso)
        self.assertEqual(bm1.id, "345")
        self.assertEqual(bm1.created_at, date_time)
        self.assertEqual(bm1.updated_at, date_time)


class TestBaseModelInstancePrint(unittest.TestCase):
    """Unittest for testing the string init method"""

    def teststringreturn(self):
        """Unittest for testing string init method."""
        bm1 = BaseModel()
        str_init =
        "[{}] ({}) {}".format("BaseModel", bm1.id, str(bm1.__dict__))
        self.assertEqual(str(bm1), str_init)

    def teststring(self):
        """Checks if the string method returns the correct output"""
        bm1 = BaseModel()
        string = "[BaseModel] ({}) {}".format(bm1.id, bm1.__dict__)
        self.assertEqual(string, str(bm1))


if __name__ == "__main__":
    unittest.main()
