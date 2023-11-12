#!/usr/bin/python3
"""
review.py unittests
"""
import unittest
from models.review import Review
import datetime


class TestReview(unittest.TestCase):
    """Review class instances and methods tests"""

    _r = Review()

    def test_class_exists(self):
        """checks if class exists"""
        res = "<class 'models.review.Review'>"
        self.assertEqual(str(type(self._r)), res)

    def test_user_inheritance(self):
        """checks if Review is a subclass of BaseModel"""
        self.assertIsInstance(self._r, Review)

    def testHasAttributes(self):
        """check if attributes exist"""
        self.assertTrue(hasattr(self._r, 'place_id'))
        self.assertTrue(hasattr(self._r, 'user_id'))
        self.assertTrue(hasattr(self._r, 'text'))
        self.assertTrue(hasattr(self._r, 'id'))
        self.assertTrue(hasattr(self._r, 'created_at'))
        self.assertTrue(hasattr(self._r, 'updated_at'))

    def test_types(self):
        """checks if attribute is the correct one"""
        self.assertIsInstance(self._r.place_id, str)
        self.assertIsInstance(self._r.user_id, str)
        self.assertIsInstance(self._r.text, str)
        self.assertIsInstance(self._r.id, str)
        self.assertIsInstance(self._r.created_at, datetime.datetime)
        self.assertIsInstance(self._r.updated_at, datetime.datetime)

if __name__ == '__main__':
    unittest.main()
