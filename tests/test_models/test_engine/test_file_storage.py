#!/usr/bin/python3
"""
Unit tests for FileStorage
"""
import unittest
import os
import json
from datetime import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """
    Unit tests for FileStorage
    """
    def setUp(self):
        """
        Setup for FileStorage
        """
        self.storage = FileStorage()
        try:
            os.rename(FileStorage._FileStorage__file_path, "test_file.json")
        except Exception:
            pass

    def tearDown(self):
        """
        Removes JSON file after testing with other methods
        """
        try:
            os.remove(FileStorage._FileStorage__file_path)
        except Exception:
            pass
        try:
            os.rename("test_file.json", FileStorage._FileStorage__file_path)
        except Exception:
            pass

    def test_all(self):
        """
        Test for all() method
        """
        self.assertIsInstance(self.storage.all(), dict)

    def test_new(self):
        """
        Test for new() method
        """
        object_1 = BaseModel()
        self.storage.new(object_1)
        key = object_1.__class__.__name__ + "." + object_1.id
        self.assertIn(key, self.storage.all())

    def test_save(self):
        """
        Test for save() method
        """
        object_1 = BaseModel()
        self.storage.new(object_1)
        self.storage.save()
        self.assertTrue(os.path.exists(FileStorage._FileStorage__file_path))

    def test_reload(self):
        """
        Test for reload() method
        """
        object_1 = BaseModel()
        self.storage.new(object_1)
        self.storage.save()
        self.storage._FileStorage__objects.clear()
        self.storage.reload()
        key = object_1.__class__.__name__ + "." + object_1.id
        self.assertIn(key, self.storage.all())

if __name__ == "__name__":
    unittest.main()