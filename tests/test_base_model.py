#!/usr/bin/python3
"""tests for base_model"""
import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """test case for BaseModel"""

    def setUp(self) -> None:
        """set up for tests"""
        self.b1 = BaseModel()

    def test_save(self):
        """test save method"""
        t1 = self.b1.updated_at
        self.b1.save()
        t2 = self.b1.updated_at
        self.assertNotEqual(t1, t2)
