#!/usr/bin/python3
"""define test class to test the json file storage,
FileStorage class and
storage instance"""

from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import os


import unittest


"""define test class to test the json file storage,
FileStorage class and
storage instance"""


class TestFileStorage(unittest.TestCase):
    def setUp(self):
        '''set up module'''
        try:
            os.remove('file.json')
        except Exception as e:
            pass
        self.base_model = BaseModel()
        self.storage = FileStorage()
        self.storage.all().clear()

    def tearDown(self):
        '''tear down module'''
        del self.base_model
        del self.storage
        try:
            os.remove('file.json')
        except Exception as e:
            pass

    def test_all(self):
        '''test all method'''
        # Assert that the initial all() method returns an empty dictionary
        self.assertEqual(self.storage.all(), {})

        # Add an object to the storage and assert that all() returns the object
        self.storage.new(self.base_model)
        self.assertEqual(self.storage.all(), {'BaseModel.{}'.format(
            self.base_model.id): self.base_model})
        self.assertEqual(type(self.storage.all()), dict)

    def test_new(self):
        '''test new method'''
        init_len = len(self.storage.all())
        new_obj = BaseModel()
        self.storage.new(new_obj)

        self.assertEqual(init_len + 1, len(self.storage.all()))

        self.assertIn(f'{new_obj.__class__.__name__}.{new_obj.id}',
                      self.storage.all().keys())

        self.assertIn(new_obj, self.storage.all().values())

    def test_reload_save(self):
        '''test reload method'''
        try:
            os.remove('file.json')
        except Exception as e:
            pass
        new_obj = BaseModel()
        new_obj.save()
        self.assertTrue(os.path.exists('file.json'))

        self.assertNotEqual(os.path.getsize('file.json'), 0)
        self.storage.reload()
        self.assertIn(f'{new_obj.__class__.__name__}.{new_obj.id}',
                      self.storage.all().keys())
        reloaded_obj = self.storage.all()[f"BaseModel.{new_obj.id}"]

        self.assertEqual(reloaded_obj.id, new_obj.id)
