#!/usr/bin/python3
""" Review class that shows new reviews"""
from models.base_model import BaseModel


class Review(Basemodel):
    """ Review subclass that inherits from Basemodel"""
    place_id = ""
    user_id = ""
    text = ""
