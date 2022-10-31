#!/usr/bin/python3
"""
contains the BaseModel class
"""
import uuid
from datetime import datetime
import models


class BaseModel:
    """
    BaseModel class propeties and method defination
    """
    def __init__(self, *args, **kwargs):
        """
        Class constructor
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                setattr(self, key, value)
                if key == "created_at" or key == "updated_at":
                    setattr(self, key, datetime.fromisoformat(value))
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def save(self):
        """
        updates and saves object to storage
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        returns dictionary representation of
        object properties
        """
        dic_format = self.__dict__.copy()
        dic_format["created_at"] = dic_format["created_at"].isoformat()
        dic_format["updated_at"] = dic_format["updated_at"].isoformat()
        dic_format["__class__"] = self.__class__.__name__
        return dic_format

    def __str__(self):
        """
        returns object string representation
        """
        out = f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
        return out
