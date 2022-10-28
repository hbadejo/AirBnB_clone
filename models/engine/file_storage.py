#!/usr/bin/python3
"""A class "FileStorage" that:

Serializes Object instances to a JSON file and
Deserializes JSON file to bac to Object instances
"""

import json
from models.base_model import BaseModel


class FileStorage():
    """Storage engine abstraction.

    Class Attributes:
        __file_path: string - path to the JSON file (ex: file.json)
        __objects: dictionary - empty but will store all objects by <class name>.id
            (ex: to store a BaseModel object with id=12121212, the key will be BaseModel.12121212)

    Class Methods:
        all(self): returns the dictionary __objects
        new(self, obj): sets in __objects the obj with key <obj class name>.id
        save(self): serializes __objects to the JSON file (path: __file_path)
        reload(self): deserializes the JSON file to __objects
            (only if the JSON file (__file_path) exists ; otherwise, do nothing.
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
        __class__.__objects[f"{objectClassName}.{obj.id}"] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        classobject = __class__.__objects
        print(f'Data from clobj: {classobject}')
        # Using Dict comprehension to implement "to_dict" on each
        # data instance in storage object
        objectdata = {data: classobject[data].to_dict()
                      for data in classobject.keys()}
        print(f'data from objdata: {objectdata}')
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
                print(objectdata)
                for data in objectdata.values():
                    cls_name = data["__class__"]
                    del data["__class__"]
                    self.new(eval(cls_name)(**data))

        except FileNotFoundError:
            return
