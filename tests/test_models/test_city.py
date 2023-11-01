#!/usr/bin/python3
"""
Unit tests for City
"""
import unittest
from models.city import City


class TestCity(unittest.TestCase):
    """
    Unit test for State
    """

    def test_city_is_instance(self):
        """
        Test that the instance is of type User
        """
        self.city_1 = City()

        self.assertIsInstance(self.city_1, City)

    def test_city_name_exist(self):
        """
        Test that the name exists
        """
        self.city_1 = City()

        self.assertEqual(self.city_1.name, "")

    def test_city_id_exist(self):
        """
        Test that the name exists
        """
        self.city_1 = City()

        self.assertEqual(self.city_1.state_id, "")