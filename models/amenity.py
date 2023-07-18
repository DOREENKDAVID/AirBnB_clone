#!usr/bin/python3
"""
Amenities module
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Subclass that inheritys from BaseModule
    containing different amenities available
    Attribute:
        name: name of amenity
    """
    name = ""
