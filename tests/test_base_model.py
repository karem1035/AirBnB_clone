"""Unit tests for the BaseModel class."""

import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Test cases for the BaseModel class."""

    def test_init(self):
        """Test the initialization of a BaseModel instance."""
        obj = BaseModel()
        self.assertIsNotNone(obj.id)
        self.assertIsNotNone(obj.created_at)
        self.assertIsNotNone(obj.updated_at)

    def test_save(self):
        """Test the save method of a BaseModel instance."""
        obj = BaseModel()
        initial_updated_at = obj.updated_at
        obj.save()
        self.assertGreater(obj.updated_at, initial_updated_at)

    def test_to_dict(self):
        """Test the to_dict method of a BaseModel instance."""
        obj = BaseModel()
        obj_dict = obj.to_dict()
        self.assertEqual(obj_dict['__class__'], 'BaseModel')
        self.assertIsInstance(obj_dict['created_at'], str)
        self.assertIsInstance(obj_dict['updated_at'], str)

    def test_empty_kwargs(self):
        """Test creating an instance with empty kwargs"""
        obj = BaseModel()
        self.assertIsNotNone(obj.id)

    def test_valid_kwargs(self):
        """Test that kwargs works"""
        kwargs = {'attr1': 'value1'}
        obj = BaseModel(**kwargs)
        self.assertEqual(obj.attr1, 'value1')


if __name__ == '__main__':
    unittest.main()
