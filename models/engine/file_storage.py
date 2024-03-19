#!/usr/bin/python3
"""File Storage"""
import json
import os
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.review import Review
from models.place import Place
from models.city import City
from models.amenity import Amenity

models_map = {"BaseModel": BaseModel,
              "User": User,
              "State": State,
              "Review": Review,
              "Place": Place,
              "City": City,
              "Amenity": Amenity
              }


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
        self.__objects[f"{d['__class__']}.{d['id']}"] = obj

    def remove(self, model, id):
        """remove an object"""
        del self.__objects[f"{model}.{id}"]

    def save(self):
        """save __objects to __file_path"""
        dict_objects = {k: v.to_dict() for k, v in self.__objects.items()}
        with open(self.__file_path, 'w') as f:
            json.dump(dict_objects, f)

    def reload(self):
        """read objects from __file_path to __objects"""
        if not os.path.exists(self.__file_path):
            return
        with open(self.__file_path) as f:
            dict_objects = json.load(f)
            self.__objects.clear()
            for k, v in dict_objects.items():
                self.__objects[k] = models_map[v['__class__']](**v)
