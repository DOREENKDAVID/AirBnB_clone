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
from models.city import City
from models.engine.file_storage import FileStorage
from models import storage
from datetime import datetime
from models.state import State


class TestCity(unittest.TestCase):
    """
    Tests for city class
    """
    @classmethod
    def setUpClass(cls):
        """ set up class method"""
        cls.city = City()
        cls.city.state_id = str(uuid.uuid4())
        cls.city.name = "Chicago"

    @classmethod
    def tearDownClass(cls):
        """clear objects after all test"""
        del cls.city
        try:
            os.remove("file.json")
        except FileNotFound:
            pass

    def test_class_exitence(self):
        """check if class exists"""
        temp = "<class 'models.city.City'>"
        self.assertEqual(str(type(self.city)), temp)

    def test_subclass_inheritance(self):
        """inheritance from BaseModel"""
        self.assertTrue(issubclass(self.city.__class__, BaseModel))

    def test_user_inheritance(self):
        """inheritance for BaseModel"""
        self.assertIsInstance(self.city, City)

    def test_doc_string(self):
        """check for class doc string"""
        self.assertIsNotNone(City.__doc__)

    def test_class_attributes(self):
        self.assertTrue('id' in self.city.__dict__)
        self.assertTrue('created_at' in self.city.__dict__)
        self.assertTrue('updated_at' in self.city.__dict__)
        self.assertTrue('name' in self.city.__dict__)

    def test_attribute_type(self):
        """checks attributes datatypes"""
        self.assertIs(type(self.city.name), str)
        self.assertIs(type(self.city.state_id), str)
        self.assertIsInstance(self.city.name, str)
        self.assertIsInstance(self.city.id, str)
        self.assertEqual(datetime, type(City().created_at))
        self.assertEqual(datetime, type(City().updated_at))

    def test_public_class_attribute(self):
        """test class attributes"""
        city_obj = City()
        self.assertEqual(str, type(city_obj.state_id))
        self.assertIn("state_id", dir(city_obj))
        self.assertNotIn("state_id", city_obj.__dict__)

        self.assertEqual(str, type(city_obj.name))
        self.assertIn("name", dir(city_obj))
        self.assertNotIn("name", city_obj.__dict__)

    def test_save(self):
        self.city.save()
        self.assertNotEqual(self.city.created_at, self.city.update_at)

    def test_to_dict(self):
        self.assertTrue("to_dict" in dir(self.city))


if __name__ == "__main__":
    unitest.main()
