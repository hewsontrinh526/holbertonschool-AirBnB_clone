#!/usr/bin/python3
""" Base Model Module for serialisation and deserialisation """
import uuid
from datetime import datetime


class BaseModel:
    """ BaseModel class"""

    def __init__(self):
        """ Initialisation of class attributes"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """ Prints given string """
        return " [{}] ({}) {}".format(
            type(self).__name__, self.id, self.__dict__)

    def save(self):
        """ Updates the public instance attribute updated_at to current"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """ Returns a dictionary which contains all key/values of __dict__"""
        new_dic = self.__dict__.copy()
        new_dic["created_at"] = self.created_at.isoformat()
        new_dic["updated_at"] = self.updated_at.isoformat()
        new_dic["__class__"] = type(self).__name__
        return new_dic
