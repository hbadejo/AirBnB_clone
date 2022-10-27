#!/usr/bin/python3
"""Create a unique File Storage instance for the Application"""

# mport file_storage.py
from models.engine.file_storage import FileStorage

# create the variable storage, an instance of FileStorage
storage = FileStorage()

# call reload() method on this variable
storage.reload()
