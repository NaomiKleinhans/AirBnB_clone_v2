#!/usr/bin/python3
"""This module creates a Amenity class"""

from models.base_model import BaseModel, Base


class Amenity(BaseModel, Base):
    """Class for managing amenity objects"""

    name = ""
