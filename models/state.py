#!/usr/bin/python3
"""
Template for State class
inheriting from BaseModel
"""
from models.base_model import BaseModel


class State(BaseModel):
    """
    Represent a state:

    Public class attributes:
        name: string -> Name of place
    """

    name = ""
