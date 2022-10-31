#!/usr/bin/python3

"""
imports json and required classes.
contains FileStorage class defination
"""
import json
from models.base_model import BaseModel
from models.user import User
from models.review import Review
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.state import State


class FileStorage:
    """
    private class properties containing json file path,
    objects to store and method definitions
    """
    __file_path = "file.json"
    __objects = dict()

    def all(self):
        """
        returns the dictionary content of __objects
        """
        return self.__objects

    def new(self, obj):
        """
        adds a new object to be stored to __objects
        """
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """
        serializes dict_storage whose values contains
        objects in their dictionary format into a json
        file
        """
        path = self.__file_path
        with open(path, "w") as file:
            dict_storage = dict()
            for key, val in self.__objects.items():
                dict_storage[key] = val.to_dict()
            json.dump(dict_storage, file)

    def reload(self):
        """
        restore objects from json file and adds
        to __objects using the new() method
        """
        path = self.__file_path
        try:
            with open(path, "r") as file:
                out = json.load(file)
                for obj in out.values():
                    cls_name = obj["__class__"]
                    del obj["__class__"]
                    obj_instance = eval(cls_name)(**obj)
                    self.new(obj_instance)
        except FileNotFoundError:
            return

