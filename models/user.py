#!/usr/bin/python3
"""
File for the user module
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    User class that inherits from BaseModel
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
