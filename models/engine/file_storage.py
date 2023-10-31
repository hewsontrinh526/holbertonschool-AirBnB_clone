#!/usr/bin/python3
""" File storage to deal with serial and unserial objects to files """
import json
import os


class FileStorage():
    """ Serialise or Deserialise data processed"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ Returns the dictionaries"""
        return(FileStorage.__objects)

    def new(self, obj):
        """create a new object """
        class_name = type(obj).__name__
        my.id = obj.id
        instance_key = class_name + "." + my_id
        FileStorage.__objects[instance_key] = obj

    def save(self):
        """ saves in json format to a file """
        my_obj_dict = {}
        for key in FileStorage.__objects:
            my_obj_dict[key] = FileStorage.__objects[key].to_dict()
        with open(FileStorage.__file_path, 'w') as file_path:
            json.dump(my_obj_dict, file_path)

    ## have to do reload
