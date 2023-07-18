#!usr/bin/python3
"""
Unitests for Amenity class
"""

import unittest
import sys
import json
import os
import uuid
from models.base_model import BaseModel
from models.review import Review
from models.engine.file_storage import FileStorage
from models import storage
from datetime import datetime


class TestReview(unittest.TestCase):
    """
    Tests for Review class
    """
    @classmethod
    def setUpClass(cls):
        """ set up class method"""
        cls.review = Review()
        cls.review.place_id = str(uuid.uuid4())
        cls.review.user_id = str(uuid.uuid4())

    @classmethod
    def tearDownClass(cls):
        """clear objects after all test"""
        del cls.review
        try:
            os.remove("file.json")
        except FileNotFound:
            pass

    def test_class_exitence(self):
        """check if class exists"""
        temp = "<class 'models.review.Review'>"
        self.assertEqual(str(type(self.review)), temp)

    def test_subclass_inheritance(self):
        """inheritance from BaseModel"""
        self.assertTrue(issubclass(self.review.__class__, BaseModel))

    def test_user_inheritance(self):
        """inheritance for BaseModel"""
        self.assertIsInstance(self.review, Review)

    def test_doc_string(self):
        """check for class doc string"""
        self.assertIsNotNone(Review.__doc__)

    def test_class_attributes(self):
        self.assertTrue('id' in self.review.__dict__)
        self.assertTrue('created_at' in self.review.__dict__)
        self.assertTrue('updated_at' in self.review.__dict__)

    def test_attribute_type(self):
        """checks attributes datatypes"""
        self.assertIs(type(self.review.place_id), str)
        self.assertIs(type(self.review.user_id), str)
        self.assertEqual(str, type(Review().id))

        self.assertEqual(datetime, type(Review().created_at))
        self.assertEqual(datetime, type(Review().updated_at))

    def test_public_class_attribute(self):
        """test class attributes"""
        review_obj = Review()

        self.assertEqual(str, type(review_obj.user_id))
        self.assertIn("user_id", dir(review_obj))
        self.assertNotIn("user_id", review_obj.__dict__)

        self.assertEqual(str, type(review_obj.place_id))
        self.assertIn("place_id", dir(review_obj))
        self.assertNotIn("place_id", review_obj.__dict__)

        self.assertEqual(str, type(review_obj.text))
        self.assertIn("text", dir(review_obj))
        self.assertNotIn("text", review_obj.__dict__)

    def test_save(self):
        self.review.save()
        self.assertNotEqual(self.review.created_at, self.review.update_at)

    def test_to_dict(self):
        self.assertTrue("to_dict" in dir(self.review))


if __name__ == "__main__":
    unitest.main()
