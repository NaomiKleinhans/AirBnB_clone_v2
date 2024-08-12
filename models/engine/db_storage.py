#!/usr/bin/python3
"""Module for DBStorage class."""
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from models.base_model import Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class DBStorage:
    """Class for interacting with the MySQL database"""
    __engine = None
    __session = None

    def __init__(self):
        """Instantiate a new DBStorage object"""
        # Create the engine and bind it to the session
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            user, passwd, host, db))
        Base.metadata.create_all(self.__engine)
        self.__session = scoped_session(sessionmaker(bind=self.__engine))

    def all(self, cls=None):
        """Query on the current database session"""
        if cls:
            objs = self.__session.query(cls).all()
        else:
            objs = self.__session.query(
                State, City, User, Place, Review, Amenity).all()
        return {obj.__class__.__name__ + "." + obj.id: obj for obj in objs}

    def new(self, obj):
        """Add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """Commit all changes of the current database session"""
        self.__session.commit()

    def reload(self):
        """Reloads the session"""
        Base.metadata.create_all(self.__engine)
        self.__session = scoped_session(sessionmaker(bind=self.__engine))

    def close(self):
        """Remove the current session"""
        self.__session.remove()
