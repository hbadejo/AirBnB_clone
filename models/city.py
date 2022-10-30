#!/usr/bin/python3
"""
Template for City class
inheriting from BaseModel
"""

from models.base_model import BaseModel


class City(BaseModel):
    """
    Represent a city

    Public class attributes:
        state_id: string -> to hold State.id
        name: string -> name of City
    """
    state_id = ""
    name = ""
