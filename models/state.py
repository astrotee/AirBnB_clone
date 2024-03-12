#!/usr/bin/python3
"""Class State"""
from models.base_model import BaseModel


class State(BaseModel):
    """Module class State"""
    name = ""

    def __init__(self, *args, **kwargs):
        """constructor"""
        super().__init__(self, *args, **kwargs)
