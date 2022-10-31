#!/usr/bin/python3
"""
Amenity class inherits from BaseModel
"""
from models.base_model import BaseModel


class User(BaseModel):
    email = ""
    password = ""
    first_name = ""
    last_name = ""
