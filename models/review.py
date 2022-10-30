#!/usr/bin/python3
"""
Template for Review class
inheriting from BaseModel
"""

from models.base_model import BaseModel


class Review(BaseModel):
    """
    Represnt a review:

    Public class attributes:
        place_id: string -> it will be the Place.id
        user_id: string -> it will be the User.id
        text: string -> Reveiw text from User
    """
    place_id = ""
    user_id = ""
    text = ""
