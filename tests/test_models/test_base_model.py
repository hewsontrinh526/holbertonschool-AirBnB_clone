#!/usr/bin/python3
"""
Unit tests for BaseModel
"""
import unittest
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    """
    Unit tests for BaseModel
    """
    def test_save_base(self):
        """
        Test to save method
        """
        base_1 = BaseModel()
        old_save = str(base_1.updated_at)
        base_1.save()
        new_save = str(base_1.updated_at)
        self.assertNotEqual(old_save, new_save)

    def test_id_base(self):
        """
        Test to generate a UUID with no input
        """
        base_1 = BaseModel()
        new_id = base_1 != None
        self.assertEqual(new_id, True)

    def test_to_dict_base(self):
        """
        Test to generate a new dict
        """
        base_1 = BaseModel()
        new_dict = base_1.to_dict()
        self.assertEqual(base_1.id, new_dict["id"])

    def test_str_base(self):
        """
        Test for __str__ method
        """
        base_1 = BaseModel()
        output = "[BaseModel] ({}) {}".format(base_1.id, base_1.__dict__)
        self.assertEqual(base_1.__str__(), output)
