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
from models.state import State
from models.engine.file_storage import FileStorage
from models import storage
from datetime import datetime


class TestState(unittest.TestCase):
    """
    Tests for state class
    """
    @classmethod
    def setUpClass(cls):
        """ set up class method"""
        cls.state = State()
        cls.state.name = "Ilinois"

    @classmethod
    def tearDownClass(cls):
        """clear objects after all test"""
        del cls.state
        try:
            os.remove("file.json")
        except FileNotFound:
            pass

    def test_class_exitence(self):
        """check if class exists"""
        temp = "<class 'models.state.State'>"
        self.assertEqual(str(type(self.state)), temp)

    def test_subclass_inheritance(self):
        """inheritance from BaseModel"""
        self.assertTrue(issubclass(self.state.__class__, BaseModel))

    def test_user_inheritance(self):
        """inheritance for BaseModel"""
        self.assertIsInstance(self.state, State)

    def test_doc_string(self):
        """check for class doc string"""
        self.assertIsNotNone(State.__doc__)

    def test_class_attributes(self):
        self.assertTrue('id' in self.state.__dict__)
        self.assertTrue('created_at' in self.state.__dict__)
        self.assertTrue('updated_at' in self.state.__dict__)
        self.assertTrue('name' in self.state.__dict__)

    def test_attribute_type(self):
        """checks attributes datatypes"""
        self.assertIs(type(self.state.name), str)
        self.assertIsInstance(self.state.name, str)

        self.assertEqual(datetime, type(State().created_at))
        self.assertEqual(datetime, type(State().updated_at))

    def test_public_class_attribute(self):
        """test class attributes"""
        state_obj = State()

        self.assertEqual(str, type(state_obj.name))
        self.assertIn("name", dir(state_obj))
        self.assertNotIn("name", state_obj.__dict__)

    def test_save(self):
        self.state.save()
        self.assertNotEqual(self.state.created_at, self.state.update_at)

    def test_to_dict(self):
        self.assertTrue("to_dict" in dir(self.state))


if __name__ == "__main__":
    unitest.main()
