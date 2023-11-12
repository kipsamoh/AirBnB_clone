#!/usr/bin/python3
""" Unittests module """
import unittest
from models.base_model import BaseModel
import os
from models import storage
from models.engine.file_storage import FileStorage
import datetime


class BaseModelTests(unittest.TestCase):
    """  Console Tests suite """

    _mymodel = BaseModel()

    def testBaseModel1(self):
        """  BaseModel instance value tests """

        self._mymodel.name = "ALX"
        self._mymodel.my_number = 89
        self._mymodel.save()
        _mymodel_json = self._mymodel.to_dict()

        self.assertEqual(self._mymodel.name, _mymodel_json['name'])
        self.assertEqual(self._mymodel.my_number, _mymodel_json['my_number'])
        self.assertEqual('BaseModel', _mymodel_json['__class__'])
        self.assertEqual(self._mymodel.id, _mymodel_json['id'])

    def testSave(self):
        """ validates whether public instance instance modules 
        attribute updated_at """
        self._mymodel.first_name = "First"
        self._mymodel.save()

        self.assertIsInstance(self._mymodel.id, str)
        self.assertIsInstance(self._mymodel.created_at, datetime.datetime)
        self.assertIsInstance(self._mymodel.updated_at, datetime.datetime)

        first_dict = self._mymodel.to_dict()

        self._mymodel.first_name = "Second"
        self._mymodel.save()
        sec_dict = self._mymodel.to_dict()

        self.assertEqual(first_dict['created_at'], sec_dict['created_at'])
        self.assertNotEqual(first_dict['updated_at'], sec_dict['updated_at'])

if __name__ == '__main__':
    unittest.main()
