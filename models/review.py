#!/usr/bin/python3
""" This is the module for the review class """
from models.base_model import BaseModel


class Review(BaseModel):
    """the class Review implementation
    """
    place_id = ""
    user_id = ""
    text = ""
