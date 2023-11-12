#!/usr/bin/python3
"""
user.py unittest
"""
import unittest
from models.city import City
import datetime


class TestCity(unittest.TestCase):
    """ city class tests for methods and instances"""

    _c = City()

    def test_class_exists(self):
        """checks if class exists"""
        self.assertEqual(str(type(self._c)), "<class 'models.city.City'>")

    def test_user_inheritance(self):
        """checks if city is subclass of BaseModel"""
        self.assertTrue(self._c, City)

    def testHasAttributes(self):
        """check whether attributes exist"""
        self.assertTrue(hasattr(self._c, 'state_id'))
        self.assertTrue(hasattr(self._c, 'name'))
        self.assertTrue(hasattr(self._c, 'id'))
        self.assertTrue(hasattr(self._c, 'created_at'))
        self.assertTrue(hasattr(self._c, 'updated_at'))

    def test_types(self):
        """checks if the attribute is the correct one"""
        self.assertIsInstance(self._c.state_id, str)
        self.assertIsInstance(self._c.name, str)
        self.assertIsInstance(self._c.id, str)
        self.assertIsInstance(self._c.created_at, datetime.datetime)
        self.assertIsInstance(self._c.updated_at, datetime.datetime)

if __name__ == '__main__':
    unittest.main()
