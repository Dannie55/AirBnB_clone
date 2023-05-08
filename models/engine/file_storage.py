#!/usr/bin/python3
"""Defines the File storage class
   serializes instances to a JSON file
   and deserialize JSON file back to instances. """
import json
import os
import uuid
from datetime import datetime
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """The FileStorage class"""
    __file_path = "file.json"
    __object = {}

    def all(self):
        """Returns a dictionary object"""
        return FileStorage.__objects

    def new(self, obj):
        """Set in __objects obj with key <obj_class_name>.id"""
        obname = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(obname, obj.id] = obj

    def save(self):
        """Serialize __objects to the JSON file __file_path."""
        adict = FileStorage.__objects
        objdict = {obj: adict[obj]. to_dict() for obj in adict.keys()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(objdict, f)

    def reload(self):
       """Deserialize the JSON file __file_path to __objects, if it exists."""
       try:
          with open(FileStorage.__file_path) as f:
              objdict = json.load(f)
              for o in objdict.values():
                  cls_name = o["__class__"]
                  del o["__class__"]
                  self.new(eval(cls_name)(**o))
        except FileNotFoundError:
            return
