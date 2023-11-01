#!/usr/bin/python3
"""
Unit tests for Review
"""
import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    """
    Unit test for Review
    """

    def test_is_instance(self):
        """
        Test that the instance is of type Review
        """
        self.review_1 = Review()

        self.assertIsInstance(self.review_1, Review)

    def test_place_id_exist(self):
        """
        Test that the name exists
        """
        self.review_1 = Review()

        self.assertEqual(self.review_1.place_id, "")

    def test_user_id_exist(self):
        """
        Test that the name exists
        """
        self.review_1 = Review()

        self.assertEqual(self.review_1.user_id, "")

    def test_text_exist(self):
        """
        Test that the name exists
        """
        self.review_1 = Review()

        self.assertEqual(self.review_1.text, "")
