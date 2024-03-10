#!/usr/bin/python3
"""base model"""
import uuid
from datetime import datetime


class BaseModel:
    """base model"""

    def __init__(self, *args, **kwargs) -> None:
        """initialize an instance"""
        if kwargs:
            kwargs.pop("__class__")
            kwargs["created_at"] = datetime.fromisoformat(kwargs["created_at"])
            kwargs["updated_at"] = datetime.fromisoformat(kwargs["updated_at"])
            self.__dict__.update(kwargs)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self) -> str:
        """a string representation of instance"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """update instance"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """a dictionary representation of instance"""
        d = self.__dict__.copy()
        d.update(__class__=self.__class__.__name__)
        d.update(created_at=self.created_at.isoformat())
        d.update(updated_at=self.updated_at.isoformat())
        return d
