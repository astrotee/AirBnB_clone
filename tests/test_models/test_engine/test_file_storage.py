#!/usr/bin/python3
"""tests for file_storage"""
import unittest
from models.base_model import BaseModel
from models import storage


class TestBaseModel(unittest.TestCase):
    """test case for FileStorage"""

    def setUp(self) -> None:
        """set up for tests"""
        self.b1 = BaseModel()

    def test_new(self):
        """test for new objects"""
        self.assertIn(f"BaseModel.{self.b1.id}", storage.all())
