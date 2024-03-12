#!/usr/bin/python3
"""Class City"""
from models.base_model import BaseModel


class City(BaseModel):
    """Module class City"""
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """constructor"""
        super().__init__(self, *args, **kwargs)
