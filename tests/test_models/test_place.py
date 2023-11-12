#!/usr/bin/python3
"""
amenity.py unittest
"""
import unittest
from models.place import Place
import datetime


class TestPlace(unittest.TestCase):
    """amenity class instances and methods tests"""

    _p = Place()

    def test_class_exists(self):
        """tests if class exists"""
        self.assertEqual(str(type(self._p)), "<class 'models.place.Place'>")

    def test_user_inheritance(self):
        """test if Place is a subclass of BaseModel"""
        self.assertIsInstance(self._p, Place)

    def testHasAttributes(self):
        """check if attr_ibutes exist"""
        self.assertTrue(hasattr(self._p, 'city_id'))
        self.assertTrue(hasattr(self._p, 'user_id'))
        self.assertTrue(hasattr(self._p, 'name'))
        self.assertTrue(hasattr(self._p, 'description'))
        self.assertTrue(hasattr(self._p, 'number_rooms'))
        self.assertTrue(hasattr(self._p, 'number_bathrooms'))
        self.assertTrue(hasattr(self._p, 'max_guest'))
        self.assertTrue(hasattr(self._p, 'price_by_night'))
        self.assertTrue(hasattr(self._p, 'latitude'))
        self.assertTrue(hasattr(self._p, 'longitude'))
        self.assertTrue(hasattr(self._p, 'amenity_ids'))
        self.assertTrue(hasattr(self._p, 'id'))
        self.assertTrue(hasattr(self._p, 'created_at'))
        self.assertTrue(hasattr(self._p, 'updated_at'))

    def test_types(self):
        """check whether the attribute is the correct one"""
        self.assertIsInstance(self._p.city_id, str)
        self.assertIsInstance(self._p.user_id, str)
        self.assertIsInstance(self._p.name, str)
        self.assertIsInstance(self._p.description, str)
        self.assertIsInstance(self._p.number_rooms, int)
        self.assertIsInstance(self._p.number_bathrooms, int)
        self.assertIsInstance(self._p.max_guest, int)
        self.assertIsInstance(self._p.price_by_night, int)
        self.assertIsInstance(self._p.latitude, float)
        self.assertIsInstance(self._p.longitude, float)
        self.assertIsInstance(self._p.amenity_ids, list)
        self.assertIsInstance(self._p.id, str)
        self.assertIsInstance(self._p.created_at, datetime.datetime)
        self.assertIsInstance(self._p.updated_at, datetime.datetime)

if __name__ == '__main__':
    unittest.main()
