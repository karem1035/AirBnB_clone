import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):

    def setUp(self):
        self.storage = FileStorage()
        self.base_model = BaseModel()
        self.base_model.save()

    def tearDown(self):
        del self.storage
        del self.base_model

    def test_all(self):
        all_objs = self.storage.all()
        self.assertIsInstance(all_objs, dict)
        self.assertIn(f"BaseModel.{self.base_model.id}", all_objs)

    def test_new(self):
        new_obj = BaseModel()
        self.storage.new(new_obj)
        all_objs = self.storage.all()
        self.assertIn(f"BaseModel.{new_obj.id}", all_objs)

    def test_save_and_reload(self):
        new_obj = BaseModel()
        self.storage.new(new_obj)
        self.storage.save()

        # Create a new storage instance for reload test
        new_storage = FileStorage()
        new_storage.reload()
        all_objs = new_storage.all()

        self.assertIn(f"BaseModel.{new_obj.id}", all_objs)
        self.assertEqual(
            all_objs[f"BaseModel.{new_obj.id}"].to_dict(), new_obj.to_dict())


if __name__ == '__main__':
    unittest.main()
