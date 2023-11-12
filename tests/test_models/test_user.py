#!/usr/bin/python3
"""
user.py unittests
"""
import unittest
from models.user import User
import datetime


class UserCase(unittest.TestCase):
    """ user class instances and methods tests"""

    _u = User()

    def test_class_exists(self):
        """checks if class exists"""
        self.assertEqual(str(type(self._u)), "<class 'models.user.User'>")

    def test_user_inheritance(self):
        """checks if User is a sub_class of Base_Model"""
        self.assertIsInstance(self._u, User)

    def testHasAttributes(self):
        """validate if attributes exist"""
        self.assertTrue(hasattr(self._u, 'email'))
        self.assertTrue(hasattr(self._u, 'password'))
        self.assertTrue(hasattr(self._u, 'first_name'))
        self.assertTrue(hasattr(self._u, 'last_name'))
        self.assertTrue(hasattr(self._u, 'id'))
        self.assertTrue(hasattr(self._u, 'created_at'))
        self.assertTrue(hasattr(self._u, 'updated_at'))

    def test_types(self):
        """checks if attribute is the correct one"""
        self.assertIsInstance(self._u.first_name, str)
        self.assertIsInstance(self._u.last_name, str)
        self.assertIsInstance(self._u.email, str)
        self.assertIsInstance(self._u.password, str)
        self.assertIsInstance(self._u.id, str)
        self.assertIsInstance(self._u.created_at, datetime.datetime)
        self.assertIsInstance(self._u.updated_at, datetime.datetime)

if __name__ == '__main__':
    unittest.main()
