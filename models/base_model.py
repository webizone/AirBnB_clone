#!/usr/bin/python3
"""Contains class defines all common attributes/methods for other classes"""
from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    """defines common attributes/methods for other classes"""
    def __init__(self, *args, **kwargs):
        """initialize attributes of BaseModel class
        """
        iso_format = "%Y-%m-%dT%H:%M:%S.%f"

        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key in ["created_at", "updated_at"]:
                    self.__dict__[key] = datetime.strptime(value, iso_format)
                else:
                    self.__dict__[key] = value
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def save(self):
        """updates public instance attr 'updated_at' with current datetime"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """returns a dictionary containing all keys/values of the __dict__
        instance
        """
        custom_dict = self.__dict__.copy()
        custom_dict["created_at"] = self.created_at.isoformat()
        custom_dict["updated_at"] = self.updated_at.isoformat()
        custom_dict["__class__"] = self.__class__.__name__
        return custom_dict

    def __str__(self):
        """modified string representation of object"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
