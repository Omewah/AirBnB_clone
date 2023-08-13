#!/usr/bin/env python3
"""Unittest for Review class"""

import unittest
import os
from datetime import datetime
from time import sleep
from models import storage
from models.review import Review
from models.base_model import BaseModel
import uuid


class TestReview(unittest.TestCase):
    """Test the review class"""

    @classmethod
    def setUpClass(cls):
        """Setup the unittest"""
        cls.review = Review()
        cls.review.user_id = str(uuid.uuid4())
        cls.review.place_id = str(uuid.uuid4())
        cls.review.text = "Lagos, Nigeria"

    @classmethod
    def tearDownClass(cls):
        """Delete the class"""
        del cls.review
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_is_subclass(self):
        self.assertTrue(issubclass(self.review.__class__, BaseModel))

    def checking_for_doc(self):
        self.assertIsNotNone(Review.__doc__)


class TestReview_instantiation(unittest.TestCase):
    """Unittests for testing instantiation"""

    def test_no_args_instantiates(self):
        self.assertEqual(Review, type(Review()))

    def test_new_instance_stored_in_objects(self):
        self.assertIn(Review(), storage.all().values())

    def test_id_is_public_str(self):
        self.assertEqual(str, type(Review().id))

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(Review().created_at))

    def test_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(Review().updated_at))

    def test_place_id_is_public_class_attribute(self):
        review = Review()
        self.assertEqual(str, type(Review.place_id))
        self.assertIn("place_id", dir(review))
        self.assertNotIn("place_id", review.__dict__)

    def test_user_id_is_public_class_attribute(self):
        review = Review()
        self.assertEqual(str, type(Review.user_id))
        self.assertIn("user_id", dir(review))
        self.assertNotIn("user_id", review.__dict__)

    def test_text_is_public_class_attribute(self):
        review = Review()
        self.assertEqual(str, type(Review.text))
        self.assertIn("text", dir(review))
        self.assertNotIn("text", review.__dict__)

    def test_two_reviews_unique_ids(self):
        review_1 = Review()
        review_2 = Review()
        self.assertNotEqual(review_1.id, review_2.id)

    def test_two_reviews_different_created_at(self):
        review_1 = Review()
        sleep(0.05)
        review_2 = Review()
        self.assertLess(review_1.created_at, review_2.created_at)

    def test_two_reviews_different_updated_at(self):
        review_1 = Review()
        sleep(0.05)
        review_2 = Review()
        self.assertLess(review_1.updated_at, review_2.updated_at)

    def test_str_representation(self):
        date_time = datetime.today()
        time_stmp = repr(date_time)
        review = Review()
        review.id = "123456"
        review.created_at = review.updated_at = date_time
        review_str = review.__str__()
        self.assertIn("[Review] (123456)", review_str)
        self.assertIn("'id': '123456'", review_str)
        self.assertIn("'created_at': " + time_stmp, review_str)
        self.assertIn("'updated_at': " + time_stmp, review_str)

    def test_args_unused(self):
        review = Review(None)
        self.assertNotIn(None, review.__dict__.values())

    def test_instantiation_with_kwargs(self):
        date_time = datetime.today()
        date_time_iso = date_time.isoformat()
        review = Review(id="345", created_at=date_time_iso, updated_at=date_time_iso)
        self.assertEqual(review.id, "345")
        self.assertEqual(review.created_at, date_time)
        self.assertEqual(review.updated_at, date_time)

    def test_instantiation_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            Review(id=None, created_at=None, updated_at=None)

class TestReview(unittest.TestCase):
    """Review model class test case"""

    @classmethod
    def setUpClass(cls):
        """Setup the unittest"""
        cls.review = Review()
        cls.review.user_id = str(uuid.uuid4())
        cls.review.place_id = str(uuid.uuid4())
        cls.review.text = "St. Petesburg"

    @classmethod
    def tearDownClass(cls):
        """Clean up the dirt"""
        del cls.review
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def testissubclass(self):
        self.assertTrue(issubclass(self.review.__class__, BaseModel))

    def checkingfordoc(self):
        self.assertIsNotNone(Review.__doc__)

    def testhasattributes(self):
        self.assertTrue('id' in self.review.__dict__)
        self.assertTrue('created_at' in self.review.__dict__)
        self.assertTrue('updated_at' in self.review.__dict__)
        self.assertTrue('user_id' in self.review.__dict__)
        self.assertTrue('place_id' in self.review.__dict__)
        self.assertTrue('text' in self.review.__dict__)

    def testattributesarestring(self):
        self.assertIs(type(self.review.user_id), str)
        self.assertIs(type(self.review.place_id), str)
        self.assertIs(type(self.review.text), str)

    def testsave(self):
        self.review.save()
        self.assertNotEqual(self.review.created_at, self.review.updated_at)

    def testtodict(self):
        self.assertTrue('to_dict' in dir(self.review))

if __name__ == "__main__":
    unittest.main()
