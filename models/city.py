!usr/bin/python3
"""
City module
"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    Subclass of BaseModel that contains diffrent city names
    in diffrent states
    Attributes:
        state_id: identification of State
        name: name of city
    """
    state_id = ""
    name = ""
