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
            name='mina1',
            my_number=2,
            created_at=datetime.now().isoformat(),
            updated_at=datetime.now().isoformat()
        )
        self.object_2 = BaseModel(
            id='456',
            name='mina2',
            my_number=1,
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
        file_path = self.storage._FileStorage__file_path

        with open(file_path, 'w') as file:
            file.write("")

    def test_objects_state(self):
        """
        Test for objects and if they are present when added
        """
        expected = ["BaseModel.{}".format(self.object_1.id)
                    , "BaseModel.{}".format(self.object_2.id)]

        for key in expected:
            self.assertIn(key, self.storage.all())

    def test_all_objects_return(self):
        """
        Test for if new method adds objects
        """
        self.assertIn("BaseModel.{}".format(self.object_1.id)
                      , self.storage.all())
        self.assertIn("BaseModel.{}".format(self.object_2.id)
                      , self.storage.all())

    def test_save(self):
        """
        Test for save method in FileStorage
        """
        self.storage.save()

        file_path = self.storage._FileStorage__file_path

        with open(file_path, 'r') as f:
            save_data = json.load(f)

        objects = self.storage.all()

        self.assertIn("BaseModel.{}".format(self.object_1.id), save_data)
        self.assertIn("BaseModel.{}".format(self.object_2.id), save_data)

    def test_reload_deserial_to_objects(self):
        """
        Test for reload method to deserialise files to objects
        """
        self.storage.reload()

        objects = self.storage.all()

        self.assertIn(f"BaseModel.{self.object_1.id}", objects)
        self.assertIn(f"BaseModel.{self.object_2.id}", objects)

    def test_reload(self):
        """
        Test for reload method
        """
        initial = self.storage.all()

        self.object_1.name = 'test_1'
        self.object_1.save()

        self.object_2.name = 'test_2'
        self.object_2.save()

        self.storage.reload()

        reloaded = self.storage.all()

        for key in initial:
            self.assertEqual(reloaded.get(key).to_dict()
                             , initial.get(key).to_dict())

