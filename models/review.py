#!usr/bin/python3
"""
Reviews module
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    subclass of BaseModule class that contains
    the user reviews about a place using a text
    Attributes:
        place_id
        user_id
        text: review
    """
    place_id = ""
    user_id = ""
    text = ""
