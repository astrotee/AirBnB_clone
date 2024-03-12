#!/usr/bin/python3
"""
Class user
"""
from models.base_model import BaseModel
import json


class User(BaseModel):
    """model class"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
