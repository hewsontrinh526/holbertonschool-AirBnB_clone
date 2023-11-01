#!/usr/bin/python3
"""
Unit tests for Amenity
"""
import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """
    Unit test for Amenity
    """

    def test_is_instance(self):
        """
        Test that the instance is of type Amenity
        """
        self.amenity_1 = Amenity()

        self.assertIsInstance(self.amenity_1, Amenity)

    def test_name_exist(self):
        """
        Test that the name exists
        """
        self.amenity_1 = Amenity()

        self.assertEqual(self.amenity_1.name, "")