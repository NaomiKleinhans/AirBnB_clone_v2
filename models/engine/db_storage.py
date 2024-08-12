from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.base_model import Base
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class DBStorage:
    """Handles storage of objects in SQLAlchemy database"""

    __engine = None
    __session = None

    def __init__(self):
        """Initialize the database engine and session"""
        self.__engine = create_engine(
            'mysql+mysqldb://username:password@localhost/db_name', pool_pre_ping=True)
        Base.metadata.create_all(self.__engine)
        self.__session = sessionmaker(bind=self.__engine)()

    def all(self, cls=None):
        """Query all objects of type cls"""
        if cls:
            if isinstance(cls, str):
                cls = eval(cls)
            objs = self.__session.query(cls).all()
        else:
            objs = []
            for cls in [State, City, User, Place, Amenity, Review]:
                objs.extend(self.__session.query(cls).all())
        return {f"{type(obj).__name__}.{obj.id}": obj for obj in objs}

    def new(self, obj):
        """Add a new object to the session"""
        self.__session.add(obj)

    def save(self):
        """Commit the session changes to the database"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete an object from the session"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Reload the session and tables"""
        self.__session = sessionmaker(bind=self.__engine)()

    def close(self):
        """Close the session"""
        self.__session.close()
