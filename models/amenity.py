#!/usr/bin/python3
"""
Template for Amenity class
inheriting from BaseModel
"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Represnt an Amenity:

    Public class attributes:
        name: string -> Amenity name
    """

    name = ""
