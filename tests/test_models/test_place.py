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
from models.place import Place
from models.engine.file_storage import FileStorage
from models import storage
from datetime import datetime
from models.state import State


class TestPlace(unittest.TestCase):
    """
    Tests for place class
    """
    @classmethod
    def setUpClass(cls):
        """ set up class method"""
        cls.place = Place()
        cls.place.city_id = str(uuid.uuid4())
        cls.place.user_id = str(uuid.uuid4())
        cls.place.name = "Miami"
        cls.place.description = "sunny weather"
        cls.place.number_rooms = 0
        cls.place.number_bathrooms = 0
        cls.place.max_guest = 0
        cls.place.price_by_night = 0
        cls.place.latitude = 0.0
        cls.place.longitude = 0.0
        cls.place.amenity_ids = []

    @classmethod
    def tearDownClass(cls):
        """clear objects after all test"""
        del cls.place
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_class_exitence(self):
        """check if class exists"""
        temp = "<class 'models.place.Place'>"
        self.assertEqual(str(type(self.place)), temp)

    def test_subclass_inheritance(self):
        """inheritance from BaseModel"""
        self.assertTrue(issubclass(self.place.__class__, BaseModel))

    def test_user_inheritance(self):
        """inheritance for BaseModel"""
        self.assertIsInstance(self.place, Place)

    def test_doc_string(self):
        """check for class doc string"""
        self.assertIsNotNone(Place.__doc__)

    def test_class_attributes(self):
        self.assertTrue('id' in self.place.__dict__)
        self.assertTrue('created_at' in self.place.__dict__)
        self.assertTrue('updated_at' in self.place.__dict__)
        self.assertTrue('name' in self.place.__dict__)

    def test_attribute_type(self):
        """checks attributes datatypes"""
        self.assertIs(type(self.place.city_id), str)
        self.assertIs(type(self.place.user_id), str)
        self.assertIs(type(self.place.name), str)
        self.assertIs(type(self.place.description), str)
        self.assertIs(type(self.place.number_rooms), int)
        self.assertIs(type(self.place.number_bathrooms), int)
        self.assertIs(type(self.place.max_guest), int)
        self.assertIs(type(self.place.price_by_night), int)
        self.assertIs(type(self.place.latitude), float)
        self.assertIs(type(self.place.longitude), float)
        self.assertIs(type(self.place.amenity_ids), list)

        self.assertIsInstance(self.place.id, str)
        self.assertEqual(datetime, type(Place().created_at))
        self.assertEqual(datetime, type(Place().updated_at))

    def test_public_class_attribute(self):
        """test class attributes"""
        self.assertTrue('city_id' in self.place.__dict__)
        self.assertTrue('user_id' in self.place.__dict__)
        self.assertTrue('name' in self.place.__dict__)
        self.assertTrue('description' in self.place.__dict__)
        self.assertTrue('number_rooms' in self.place.__dict__)
        self.assertTrue('number_bathrooms' in self.place.__dict__)
        self.assertTrue('max_guest' in self.place.__dict__)
        self.assertTrue('price_by_night' in self.place.__dict__)
        self.assertTrue('latitude' in self.place.__dict__)
        self.assertTrue('longitude' in self.place.__dict__)
        self.assertTrue('amenity_ids' in self.place.__dict__)

    def test_save(self):
        self.place.save()
        self.assertNotEqual(self.place.created_at, self.place.update_at)

    def test_to_dict(self):
        self.assertTrue("to_dict" in dir(self.place))


if __name__ == "__main__":
    unitest.main()
