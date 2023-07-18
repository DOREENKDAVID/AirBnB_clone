#!usr/bin/python3
"""
Unitests for Amenity class
"""

import unittest
import sys
import json
import os
from models.base_model import BaseModel
from models.amenity import Amenity
from models.engine.file_storage import FileStorage
from models import storage
from datetime import datetime


class TestAmenity(unittest.TestCase):
    """
    Tests for Amenity class
    """
    @classmethod
    def setUpClass(cls):
        """ set up class method"""
        cls.amenity = Amenity()
        cls.amenity.name = "gym"

    @classmethod
    def tearDownClass(cls):
        """clear objects after all test"""
        del cls.amenity
        try:
            os.remove("file.json")
        except FileNotFound:
            pass

    def test_class_exitence(self):
        """check if class exists"""
        temp = "<class 'models.amenity.Amenity'>"
        self.assertEqual(str(type(self.amenity)), temp)

    def test_subclass_inheritance(self):
        """inheritance from BaseModel"""
        self.assertTrue(issubclass(self.amenity.__class__, BaseModel))

    def test_user_inheritance(self):
        """inheritance for BaseModel"""
        self.assertIsInstance(self.amenity, Amenity)

    def test_doc_string(self):
        """check for class doc string"""
        self.assertIsNotNone(Amenity.__doc__)

    def test_class_attributes(self):
        self.assertTrue('id' in self.amenity.__dict__)
        self.assertTrue('created_at' in self.amenity.__dict__)
        self.assertTrue('updated_at' in self.amenity.__dict__)
        self.assertTrue('name' in self.amenity.__dict__)

    def test_name_attribute(self):
        amenity_obj = Amenity()
        self.assertEqual(str, type(amenity_obj.name))
        self.assertIn("name", dir(amenity_obj))
        self.assertNotIn("name", amenity_obj.__dict__)

    def test_attribute_type(self):
        """checks attributes datatypes"""
        self.assertIs(type(self.amenity.name), str)
        self.assertIsInstance(self.amenity.name, str)
        self.assertIsInstance(self.amenity.id, str)

        self.assertEqual(datetime, type(Amenity().created_at))
        self.assertEqual(datetime, type(Amenity().updated_at))

    def test_save(self):
        self.amenity.save()
        self.assertNotEqual(self.amenity.created_at, self.amenity.update_at)

    def test_to_dict(self):
        self.assertTrue("to_dict" in dir(self.amenity))


if __name__ == "__main__":
    unitest.main()
