#!/usr/bin/python3
"""
Template for Place class
inheriting from BaseModel
"""

from models.base_model import BaseModel


class Place(BaseModel):
    """Represent a place.

    Public class attributes::
        city_id: string -> it will be the City id
        user_id: string -> it will be the User id
        name: string -> name of place
        description: string -> Description of place
        number_rooms: integer -> Number of available rooms
        number_bathrooms: integer -> Number of bathromms
        max_guest: integer -> Allowable person
        price_by_night: integer -> Price of accomodation per night
        latitude: float -> Latitude location of place
        longitude: float -> Longitude location of place
        amenity_ids: list of string -> List of Amenity id.
    """

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
