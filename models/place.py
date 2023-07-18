#!usr/bin/python3
"""
Place Module
"""
from models.base_model import BaseModel


class Place(BaseModel):
    """
    subclass of BaseModule that contains details
    about the place the user checked in to
    Attributes:
    name = "" = name of the place
    city_id = "" = city  identification in the place
    user_id = "" = user identification
    description = "" = description of the place
    number_rooms = 0 = number of rooms
    number_bathrooms = 0 = number of bathrooms
    max_guests = 0 = max number of guest
    price_by_night = 0 = cost of a place by night
    latitude = 0.0 =  longitude of the location in map
    longitude = 0.0 longitude of the location in map
    amenity_ids = [] = list of amenities
    """
    name = ""
    city_id = ""
    user_id = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
