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
        Setup for the FileStorage class so that it can be initialised
        """
        self.storage = FileStorage()
        self.temp_file_path = "temp_file.json"
        self.object_1 = BaseModel(
            id='123',
            name='test1',
            my_number=42,
            created_at=datetime.now().isoformat(),
            updated_at=datetime.now().isoformat()
        )
        self.object_2 = BaseModel(
            id='456',
            name='test2',
            my_number=24,
            created_at=datetime.now().isoformat(),
            updated_at=datetime.now().isoformat()
        )
        self.storage.new(self.object_1)
        self.storage.new(self.object_2)
        self.storage.save()
        self.storage.reload()

    def tearDown(self):
        """
        Clean up after completion of tests
        """
        if os.path.exists(self.temp_file_path):
            os.remove(self.temp_file_path)

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

    def test_save(self):
        """
        Test for save method in FileStorage
        """
        self.storage.save()
        with open(self.storage._FileStorage__file_path, 'r') as f:
            save_data = json.load(f)
        objects = self.storage.all()
        self.assertIn(f"BaseModel.{self.object_1.id}", save_data)
        self.assertIn(f"BaseModel.{self.object_2.id}", save_data)
