#!/usr/bin/python3
""" Unittests modules """
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage
import os
import json


class FileStorageTests(unittest.TestCase):
    """ File_Storage Tests suites """

    my_model = BaseModel()

    def testClassInstance(self):
        """ Checks for instances """
        self.assertIsInstance(storage, FileStorage)

    def testStoreBaseModel(self):
        """ save and reload test functions """
        self.my_model.full_name = "BaseModel Instance"
        self.my_model.save()
        bm_dict = self.my_model.to_dict()
        all_objs = storage.all()

        key = bm_dict['__class__'] + "." + bm_dict['id']
        self.assertEqual(key in all_objs, True)

    def testStoreBaseModel2(self):
        """ save, reload and update tests functions """
        self.my_model.my_name = "First name"
        self.my_model.save()
        bm_dict = self.my_model.to_dict()
        all_objs = storage.all()

        key = bm_dict['__class__'] + "." + bm_dict['id']

        self.assertEqual(key in all_objs, True)
        self.assertEqual(bm_dict['my_name'], "First name")

        create_1 = bm_dict['created_at']
        update_1 = bm_dict['updated_at']

        self.my_model.my_name = "Second name"
        self.my_model.save()
        bm_dict = self.my_model.to_dict()
        all_objs = storage.all()

        self.assertEqual(key in all_objs, True)

        create_2 = bm_dict['created_at']
        update_2 = bm_dict['updated_at']

        self.assertEqual(create_1, create_2)
        self.assertNotEqual(update_1, update_2)
        self.assertEqual(bm_dict['my_name'], "Second name")

    def testHasAttributes(self):
        """checks if attributes exist"""
        self.assertEqual(hasattr(FileStorage, '_FileStorage__file_path'), True)
        self.assertEqual(hasattr(FileStorage, '_FileStorage__objects'), True)

    def testsave(self):
        """checks if JSON file exists"""
        self.my_model.save()
        self.assertEqual(os.path.exists(storage._FileStorage__file_path), True)
        self.assertEqual(storage.all(), storage._FileStorage__objects)

    def testreload(self):
        """tests if the reload functions works """
        self.my_model.save()
        self.assertEqual(os.path.exists(storage._FileStorage__file_path), True)
        dobj = storage.all()
        FileStorage._FileStorage__objects = {}
        self.assertNotEqual(dobj, FileStorage._FileStorage__objects)
        storage.reload()
        for key, value in storage.all().items():
            self.assertEqual(dobj[key].to_dict(), value.to_dict())

    def testSaveSelf(self):
        """ verifies if save_self is executed successful """
        msg = "save() takes 1 positional argument but 2 were given"
        with self.assertRaises(TypeError) as e:
            FileStorage.save(self, 100)

        self.assertEqual(str(e.exception), msg)

    def test_save_FileStorage(self):
        """ checks if new_method is working fine """
        var_1 = self.my_model.to_dict()
        new_key = var_1['__class__'] + "." + var_1['id']
        storage.save()
        with open("file.json", 'r') as fd:
            var_2 = json.load(fd)
        new = var_2[new_key]
        for key in new:
            self.assertEqual(var_1[key], new[key])

if __name__ == '__main__':
    unittest.main()
