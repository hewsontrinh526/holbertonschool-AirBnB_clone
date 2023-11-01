#!/usr/bin/python3
"""
Unit tests for User
"""
import unittest
from models.base_model import BaseModel
from models.user import User


class Testuser(unittest.TestCase):
    """
    Unit test for User
    """

    def setUp(self):
        """
        Setup for unittest testing
        """
        self.user_1 = User()

    def test_is_instance(self):
        """
        Test that the instance if of type User
        """
        self.assertIsInstance(self.user_1, User)

    def test_inheritance(self):
        """
        Test that User inherits from the the class BaseModel
        """
        self.assertTrue(issubclass(User, BaseModel))

    def test_empty_attributes(self):
        """
        Test for the initialisation of the User attributes
        """
        self.assertEqual(self.user_1.email, "")
        self.assertEqual(self.user_1.password, "")
        self.assertEqual(self.user_1.first_name, "")
        self.assertEqual(self.user_1.last_name, "")
