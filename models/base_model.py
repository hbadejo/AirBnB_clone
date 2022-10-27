#!/usr/bin/python3
"""
BaseModel is a class that defines all common attributes/methods for other classes:
"""

from datetime import datetime
from uuid import uuid4
import models


class BaseModel():
    """
    A base model for ALX AirBnB Project
    """

    def __init__(self, *args, **kwargs) -> None:
        """Initialize a new BaseModel.

        Args:
            **kwargs (dict): Key/value pairs of attributes.
            *args (any): won’t be used
        """
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        # Converting time string to datetime object
        # Using strptime(date_string, format)
        dtformat = "%Y-%m-%dT%H:%M:%S.%f"
        if kwargs is not None:
            for key, val in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.strptime(val, dtformat)
                else:
                    self.__dict__[key] = val
        else:
            models.storage.new(self)

    def save(self):
        """updates the public instance attribute updated_at with the current datetime"""
        self.updated_at = datetime.now()
        models.storage.save()

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
