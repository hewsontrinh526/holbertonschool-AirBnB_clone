#!/usr/bin/python3
"""
Unit tests for FileStorage
"""
import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """
    Unit tests for FileStorage
    """
    def setUp(self):
        """
        Setup for the FileStorage class so that it can be initialised
        """
        self.storage = FileStorage()

    def test_file_path(self):
        """
        Test to see if the serialised file is saved on the correct path
        """
        file_path_1 = self.storage._FileStorage__file_path
        self.assertEqual(file_path_1, "file.json")

    def test_objects_initial_state(self):
        """
        Test for initial state of __object attribute
        """
        obj = BaseModel()
        self.storage.new(obj)
        expected_key = "{}.{}".format(obj.__class__.__name__, obj.id)
        object_1 = self.storage._FileStorage__objects
        self.assertIn(expected_key, object_1)
        self.assertEqual(object_1[expected_key], obj)

    def test_all_objects_return(self):
        """
        Test for all objects returning properly
        """
        self.storage._FileStorage__objects = {
            "Object1": {"id": "1", "name": "Object 1"},
            "Object2": {"id": "2", "name": "Object 2"},
            "Object3": {"id": "3", "name": "Object 3"}
        }
        expected_output = {
            "Object1": {"id": "1", "name": "Object 1"},
            "Object2": {"id": "2", "name": "Object 2"},
            "Object3": {"id": "3", "name": "Object 3"}
        }
        self.assertEqual(self.storage.all(), expected_output)
