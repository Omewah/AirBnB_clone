#!/usr/bin/python3
"""Unittests for state class"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.state import State
from models import storage
from models.base_model import BaseModel

class TestStateinstantiation(unittest.TestCase):
    """Unittests for instantiation"""

    def testnoargsinstantiates(self):
        self.assertEqual(State, type(State()))

    def testnewinstancestoredinobjects(self):
        self.assertIn(State(), models.storage.all().values())

    def testidispublicstring(self):
        self.assertEqual(str, type(State().id))

    def testcreated_atispublicdatetime(self):
        self.assertEqual(datetime, type(State().created_at))

    def testupdated_atispublicdatetime(self):
        self.assertEqual(datetime, type(State().updated_at))

    def testnameispublicclassattribute(self):
        state = State()
        self.assertEqual(str, type(State.name))
        self.assertIn("name", dir(state))
        self.assertNotIn("name", state.__dict__)

    def testtwostatesuniqueid(self):
        state_1 = State()
        state_2 = State()
        self.assertNotEqual(state_1.id, state_2.id)

    def testtwostatesdifferentcreated_at(self):
        state_1 = State()
        sleep(0.05)
        state_2 = State()
        self.assertLess(state_1.created_at, state_2.created_at)

    def testtwostatesdifferentupdated_at(self):
        state_1 = State()
        sleep(0.05)
        state_2 = State()
        self.assertLess(state_1.updated_at, state_2.updated_at)

    def teststringrepr(self):
        date_time = datetime.today()
        time_stmp = repr(date_time)
        state = State()
        state.id = "123456"
        state.created_at = state.updated_at = date_time
        ststr = state.__str__()
        self.assertIn("[State] (123456)", ststr)
        self.assertIn("'id': '123456'", ststr)
        self.assertIn("'created_at': " + time_stmp, ststr)
        self.assertIn("'updated_at': " + time_stmp, ststr)

    def testargsunused(self):
        state = State(None)
        self.assertNotIn(None, state.__dict__.values())

    def testinstantiationwithkwargs(self):
        date_time = datetime.today()
        date_time_iso = date_time.isoformat()
        state = State(id="345", created_at=date_time_iso, updated_at=date_time_iso)
        self.assertEqual(state.id, "345")
        self.assertEqual(state.created_at, date_time)
        self.assertEqual(state.updated_at, date_time)

    def testinstantiationwithNonekwargs(self):
        with self.assertRaises(TypeError):
            State(id=None, created_at=None, updated_at=None)

    def testinstantiationinit(self):
        """Unittest for instantiation"""

        state = State()
        self.assertEqual(str(type(state)), "<class 'models.state.State'>")
        self.assertIsInstance(state, State)
        self.assertTrue(issubclass(type(state), BaseModel))
    

if __name__ == "__main__":
    unittest.main()
