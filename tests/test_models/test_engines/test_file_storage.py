#!/usr/bin/python3
"""Unittests for file storage class"""
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage
import os
import json


class FileStorageTests(unittest.TestCase):
    """Tests the File Storage class model"""

    mod = BaseModel()

    def testClassInstance(self):
        """Tests for the class instance"""
        self.assertIsInstance(storage, FileStorage)

    def testStoreBaseModel(self):
        """Checks the save and reload attributes"""
        self.mod.full_name = "BaseModel Instance"
        self.mod.save()
        mod_dict = self.mod.to_dict()
        store_alls = storage.all()

        key_kwarg = mod_dict['__class__'] + "." + mod_dict['id']
        self.assertEqual(key_kwarg in store_alls, True)

    def testStoreBaseModel2(self):
        """Checks save + reload + update attributes"""
        self.mod.my_name = "First name"
        self.mod.save()
        mod_dict = self.mod.to_dict()
        store_alls = storage.all()

        key_kwarg = mod_dict['__class__'] + "." + mod_dict['id']

        self.assertEqual(key_kwarg in store_alls, True)
        self.assertEqual(mod_dict['my_name'], "First name")

        c1 = mod_dict['created_at']
        u1 = mod_dict['updated_at']

        self.mod.my_name = "Second name"
        self.mod.save()
        mod_dict = self.mod.to_dict()
        store_alls = storage.all()

        self.assertEqual(key_kwarg in store_alls, True)

        c2 = mod_dict['created_at']
        u2 = mod_dict['updated_at']

        self.assertEqual(c1, c2)
        self.assertNotEqual(u1, u2)
        self.assertEqual(mod_dict['my_name'], "Second name")

    def testHasAttributes(self):
        """Checks if storage attributes exists"""
        self.assertEqual(hasattr(FileStorage, '_FileStorage__file_path'), True)
        self.assertEqual(hasattr(FileStorage, '_FileStorage__objects'), True)

    def testsave(self):
        """Checks for JSON"""
        self.mod.save()
        self.assertEqual(os.path.exists(storage._FileStorage__file_path), True)
        self.assertEqual(storage.all(), storage._FileStorage__objects)

    def testreload(self):
        """Check reload"""
        self.mod.save()
        self.assertEqual(os.path.exists(storage._FileStorage__file_path), True)
        reload_obj = storage.all()
        FileStorage._FileStorage__objects = {}
        self.assertNotEqual(reload_obj, FileStorage._FileStorage__objects)
        storage.reload()
        for key_kwarg, value_kwarg in storage.all().items():
            self.assertEqual(reload_obj[key_kwarg].to_dict(), value_kwarg.to_dict())

    def testSaveSelf(self):
        """Check save"""
        message = "save() takes 1 positional argument but 2 were given"
        with self.assertRaises(TypeError) as err:
            FileStorage.save(self, 100)

        self.assertEqual(str(err.exception), message)


if __name__ == '__main__':
    unittest.main()