#!/usr/bin/python3
"""Serialize instances to a JSON file +
deserializes JSON file to instances.
"""

import json
import os
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

class_dict = {
    "BaseModel": BaseModel,
    "User": User,
    "Place": Place,
    "Amenity": Amenity,
    "City": City,
    "Review": Review,
    "State": State
}


class FileStorage:
    """The file storage class"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the object dictionary"""
        return type(self).__objects

    def new(self, new_inst):
        """This adds new objects instance in the dictionary"""
        if new_inst.id in type(self).__objects:
            print("exists")
            return
        obj_key = "{}.{}".format(new_inst.__class__.__name__, new_inst.id)
        type(self).__objects[obj_key] = new_inst

    def save(self):
        """This serializes object instances to the JSON file"""
        serial_dict = []
        for obj_inst in type(self).__objects.values():
            serial_dict.append(obj_inst.to_dict())
        with open(type(self).__file_path, "w", encoding='utf-8') as file:
            json.dump(serial_dict, file)

    def reload(self):
        """This deserializes the JSON file"""
        if os.path.exists(type(self).__file_path) is True:
            return
            try:
                with open(type(self).__file_path, "r") as file:
                    deserial = json.load(file)
                    for obj_key, obj_inst in deserial.items():
                        inst =
                        self.class_dict[obj_inst['__class__']](**obj_inst)
                        type(self).__objects[obj_key] = inst
            except Exception:
                pass
