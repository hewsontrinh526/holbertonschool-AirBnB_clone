#!/usr/bin/python3
"""
Unit tests for BaseModel
"""
import unittest
from models.state import State


class TestState(unittest.TestCase):
    """
    Unit test for State
    """

    def test_is_instance(self):
        """
        Test that the instance is of type State
        """
        self.state_1 = State()

        self.assertIsInstance(self.state_1, State)

    def test_name_exist(self):
        """
        Test that the name exists
        """
        self.state_1 = State()

        self.assertEqual(self.state_1.name, "")
