#!/usr/bin/python3
"""Amenity Class"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """module class amenity"""
    name = ""

    def __init__(self, *args, **kwargs):
        """constructor"""
        super().__init__(self, *args, **kwargs)
