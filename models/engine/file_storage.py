#!/usr/bin/python3
""" File storage to deal with serial and unserial objects to files """
import json
import os


class FileStorage:
    """ Serialise or Deserialise data processed"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ Returns the dictionaries"""
        return self.__objects

    def new(self, obj):
        """create a new object """
        name = type(obj).__name__
        obj_id = str(obj.id)
        instance_key = name + "." + obj_id
        self.__objects[instance_key] = obj

    def save(self):
        """ saves in json format to a file """
        my_obj_dict = {}
        for key in self.__objects:
            my_obj_dict[key] = self.__objects[key].to_dict()
        with open(self.__file_path, 'w') as f:
            json.dump(my_obj_dict, f)

    def reload(self):
        """
        Deserialisation the JSON file to __objects
        """
        from models.base_model import BaseModel
        from models.user import User
        reloaded_dict = {}
        try:
            with open(self.__file_path, "r") as f:
                reloaded_dict = json.load(f)
        except:
            reloaded_dict = {}
            pass
        for key, obj in reloaded_dict.items():
            self.__objects[key] = BaseModel(**obj)
