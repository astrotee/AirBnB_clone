#!/usr/bin/python3
"""File Storage"""
import json
import os
from models.user import User


class FileStorage:
    """File Storage model"""
    __file_path = "file.json"
    __objects = dict()

    def all(self) -> dict:
        """return the objects"""
        return self.__objects

    def new(self, obj):
        """add a new object"""
        d = obj.to_dict()
        self.__objects[f"{d['__class__']}.{d['id']}"] = d

    def remove(self, model, id):
        """remove an object"""
        del self.__objects[f"{model}.{id}"]

    def save(self):
        """save __objects to __file_path"""
        with open(self.__file_path, 'w') as f:
            json.dump(self.__objects, f)

    def reload(self):
        """read objects from __file_path to __objects"""
        if not os.path.exists(self.__file_path):
            return
        with open(self.__file_path) as f:
            self.__objects = json.load(f)
