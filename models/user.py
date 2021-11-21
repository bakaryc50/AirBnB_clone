#!/usr/bin/python3
""" This is the module for the user class """
from models.base_model import BaseModel


class User(BaseModel):
    """the class User implementation
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
