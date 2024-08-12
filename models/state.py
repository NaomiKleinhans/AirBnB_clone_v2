#!/usr/bin/python3
"""This module creates a State class"""

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import models
from models.city import City


class State(BaseModel, Base):
    """Class for managing state objects"""
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)

    cities = relationship("City", backref="state",
                          cascade="all, delete-orphan")

    @property
    def cities(self):
        """Getter for the cities linked to the current state"""
        if models.storage_type != 'db':
            return [city for city in models.storage.all(City).values()
                    if city.state_id == self.id]
        return self.cities
