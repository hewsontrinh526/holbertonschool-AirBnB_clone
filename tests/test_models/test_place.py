#!/usr/bin/python3
"""
Unit tests for Place
"""
import unittest
from models.place import Place


class TestPlace(unittest.TestCase):
    """
    Unit test for Place
    """

    def test_is_instance(self):
        """
        Test that the instance is of type Amenity
        """
        self.place_1 = Place()

        self.assertIsInstance(self.place_1, Place)

    def test_city_id_exist(self):
        """
        Test that the name exists
        """
        self.place_1 = Place()

        self.assertEqual(self.place_1.city_id, "")

    def test_user_id_exist(self):
        """
        Test that the name exists
        """
        self.place_1 = Place()

        self.assertEqual(self.place_1.user_id, "")

    def test_name_exist(self):
        """
        Test that the name exists
        """
        self.place_1 = Place()

        self.assertEqual(self.place_1.name, "")

    def test_description_exist(self):
        """
        Test that the name exists
        """
        self.place_1 = Place()

        self.assertEqual(self.place_1.description, "")

    def test_number_rooms_exist(self):
        """
        Test that the name exists
        """
        self.place_1 = Place()

        self.assertEqual(self.place_1.number_rooms, 0)

    def test_number_bathrooms_exist(self):
        """
        Test that the name exists
        """
        self.place_1 = Place()

        self.assertEqual(self.place_1.number_bathrooms, 0)

    def test_max_guest_exist(self):
        """
        Test that the name exists
        """
        self.place_1 = Place()

        self.assertEqual(self.place_1.max_guest, 0)

    def test_price_by_night_exist(self):
        """
        Test that the name exists
        """
        self.place_1 = Place()

        self.assertEqual(self.place_1.price_by_night, 0)

    def test_latitude_exist(self):
        """
        Test that the name exists
        """
        self.place_1 = Place()

        self.assertEqual(self.place_1.latitude, 0)

    def test_longitude_exist(self):
        """
        Test that the name exists
        """
        self.place_1 = Place()

        self.assertEqual(self.place_1.longitude, 0)

    def test_amenity_ids_exist(self):
        """
        Test that the name exists
        """
        self.place_1 = Place()

        self.assertEqual(self.place_1.amenity_ids, [])
