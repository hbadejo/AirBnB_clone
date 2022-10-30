#!/usr/bin/python3
"""
Template for User class
inheriting from BaseModel
"""

from models.base_model import BaseModel


class User(BaseModel):
    """
    Represent a User:

    Public class attributes:
        email: string -> Email of User
        password: string -> User password
        first_name: string -> User First Name
        last_name: string -> User last Name
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
