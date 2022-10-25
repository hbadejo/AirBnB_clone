#!/usr/bin/python3
"""
BaseModel is a class that defines all common attributes/methods for other classes:
"""

from datetime import datetime
from uuid import uuid4


class BaseModel():
    """
    A base model for ALX AirBnB Project
    """

    def __init__(self, *args, **kwargs) -> None:
        """Initialize a new BaseModel.

        Args:
            **kwargs (dict): Key/value pairs of attributes.
            *args (any): 
        """
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def save(self):
        """updates the public instance attribute updated_at with the current datetime"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Returns a dictionary containing all keys/values of __dict__ of the instance

        This method will be the first piece of the serialization/deserialization process: 
        create a dictionary representation with “simple object type” of our BaseModel
        """
        instance_attribute = self.__dict__.copy()
        instance_attribute["created_at"] = self.created_at.isoformat()
        instance_attribute["updated_at"] = self.updated_at.isoformat()
        instance_attribute["__class__"] = self.__class__.__name__
        return instance_attribute

    def __str__(self):
        """Return the informal str representation of the BaseModel instance."""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
