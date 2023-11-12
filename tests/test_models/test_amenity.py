#!/usr/bin/python3
"""
 Amenity class tests
"""
import unittest
from models.amenity import Amenity
import datetime


class TestAmenity(unittest.TestCase):
    """Tests methods and instances in the amenity class"""

    x = Amenity()

    def test_class_exists(self):
        """checks whether class exists"""
        m = "<class 'models.amenity.Amenity'>"
        self.assertEqual(str(type(self.x)), m)

    def test_user_inheritance(self):
        """checks whether Amenity is a sub_class of BaseModel"""
        self.assertIsInstance(self.x, Amenity)

    def testHasAttributes(self):
        """check if attributes exist"""
        self.assertTrue(hasattr(self.x, 'name'))
        self.assertTrue(hasattr(self.x, 'id'))
        self.assertTrue(hasattr(self.x, 'created_at'))
        self.assertTrue(hasattr(self.x, 'updated_at'))

    def test_types(self):
        """validates the type of attribute is the correct one"""
        self.assertIsInstance(self.x.name, str)
        self.assertIsInstance(self.x.id, str)
        self.assertIsInstance(self.x.created_at, datetime.datetime)
        self.assertIsInstance(self.x.updated_at, datetime.datetime)

if __name__ == '__main__':
    unittest.main()
