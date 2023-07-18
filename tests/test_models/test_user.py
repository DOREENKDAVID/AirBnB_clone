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
from models.engine.file_storage import FileStorage
from models import storage
from datetime import datetime
from models.user import User


class TestUser(unittest.TestCase):
    """
    Tests for user class
    """
    @classmethod
    def setUpClass(cls):
        """ set up class method"""
        cls.user = User()
        cls.user.email = "johndoe@domain.com"
        cls.user.first_name = "john"
        cls.user.last_name = "doe"

    @classmethod
    def tearDownClass(cls):
        """clear objects after all test"""
        del cls.user
        try:
            os.remove("file.json")
        except FileNotFound:
            pass

    def test_class_exitence(self):
        """check if class exists"""
        temp = "<class 'models.user.User'>"
        self.assertEqual(str(type(self.user)), temp)

    def test_subclass_inheritance(self):
        """inheritance from BaseModel"""
        self.assertTrue(issubclass(self.user.__class__, BaseModel))

    def test_user_inheritance(self):
        """inheritance for BaseModel"""
        self.assertIsInstance(self.user, User)

    def test_doc_string(self):
        """check for class doc string"""
        self.assertIsNotNone(User.__doc__)

    def test_inherited_class_attributes(self):
        self.assertTrue('id' in self.user.__dict__)
        self.assertTrue('created_at' in self.user.__dict__)
        self.assertTrue('updated_at' in self.user.__dict__)

    def test_attribute_type(self):
        """checks attributes datatypes"""
        self.assertIs(type(self.user.email), str)
        self.assertIs(type(self.user.password), str)
        self.assertIsInstance(self.user.first_name, str)
        self.assertIsInstance(self.user.last_name, str)
        self.assertEqual(datetime, type(User().created_at))
        self.assertEqual(datetime, type(User().updated_at))

    def test_public_class_attribute(self):
        """test class attributes"""
        user_obj = User()

        self.assertEqual(str, type(user_obj.email))
        self.assertIn("email", dir(user_obj))
        self.assertNotIn("email", user_obj.__dict__)

        self.assertEqual(str, type(user_obj.password))
        self.assertIn("password", dir(user_obj))
        self.assertNotIn("password", user_obj.__dict__)

        self.assertEqual(str, type(user_obj.first_name))
        self.assertIn("first_name", dir(user_obj))
        self.assertNotIn("first_name", user_obj.__dict__)

        self.assertEqual(str, type(user_obj.last_name))
        self.assertIn("last_name", dir(user_obj))
        self.assertNotIn("last_name", user_obj.__dict__)

    def test_save(self):
        self.user.save()
        self.assertNotEqual(self.user.created_at, self.user.update_at)

    def test_to_dict(self):
        self.assertTrue("to_dict" in dir(self.user))


if __name__ == "__main__":
    unitest.main()
