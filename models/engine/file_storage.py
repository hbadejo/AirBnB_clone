#!/usr/bin/python3
"""A class "FileStorage" that:

Serializes Object instances to a JSON file and
Deserializes JSON file to bac to Object instances
"""

import json
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State


class FileStorage():
    """Storage engine abstraction.

    Class Attributes:
        __file_path: string - path to the JSON file (ex: file.json)
        __objects: dictionary - empty but will store all
            objects by <class name>.id

    Class Methods:
        all(self): returns the dictionary __objects
        new(self, obj): sets in __objects the obj with key <obj class name>.id
        save(self): serializes __objects to the JSON file (path: __file_path)
        reload(self): deserializes the JSON file to __objects
            (only if the JSON file (__file_path) exists; otherwise, do nothing.
            If the file doesn’t exist, no exception should be raised)
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return __class__.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        objectClassName = obj.__class__.__name__
        self.__class__.__objects[f"{objectClassName}.{obj.id}"] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        classobject = __class__.__objects
        # Using Dict comprehension to implement "to_dict" on each
        # data instance in storage object
        objectdata = {data: classobject[data].to_dict()
                      for data in classobject.keys()}
        # Data serialization
        with open(__class__.__file_path, "w") as s_file:
            json.dump(objectdata, s_file)
        # print(objectdata)

    def reload(self):
        """
        Deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists ; otherwise, do nothing.
        If the file doesn’t exist, no exception should be raised)
        """
        try:
            with open(__class__.__file_path) as s_file:
                objectdata = json.load(s_file)
                for data in objectdata.values():
                    className = data["__class__"]
                    del data["__class__"]
                    # Without the "**", the id value is recreated
                    # leading to a different id for all data in storage
                    # at every instantiation of reload
                    self.new(eval(className)(**data))
        except FileNotFoundError:
            return
