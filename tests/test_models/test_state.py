#!/usr/bin/python3
"""
amenity.py unittests
"""
import unittest
from models.state import State
import datetime


class TestState(unittest.TestCase):
    """ State class instances and methods test """

    _s = State()

    def test_class_exists(self):
        """checks if class exists"""
        _res = "<class 'models.state.State'>"
        self.assertEqual(str(type(self._s)), _res)

    def test_user_inheritance(self):
        """checks whether State is a subclass of BaseModel"""
        self.assertIsInstance(self._s, State)

    def testHasAttributes(self):
        """check if attributes exist"""
        self.assertTrue(hasattr(self._s, 'name'))
        self.assertTrue(hasattr(self._s, 'id'))
        self.assertTrue(hasattr(self._s, 'created_at'))
        self.assertTrue(hasattr(self._s, 'updated_at'))

    def test_types(self):
        """tests if the type of the attribute is the correct one"""
        self.assertIsInstance(self._s.name, str)
        self.assertIsInstance(self._s.id, str)
        self.assertIsInstance(self._s.created_at, datetime.datetime)
        self.assertIsInstance(self._s.updated_at, datetime.datetime)

if __name__ == '__main__':
    unittest.main()
