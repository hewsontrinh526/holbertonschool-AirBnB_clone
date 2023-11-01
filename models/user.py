#!/usr/bin/python3
""" Module with User class that inherits from Base Model"""

from models.base_model import BaseModel


class User(BaseModel):
    """ Class attributes that describe the user"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
