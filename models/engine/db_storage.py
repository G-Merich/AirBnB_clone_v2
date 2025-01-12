#!/usr/bin/python3


from os import getenv
from models.base_model import Base
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from sqlalchemy import create_engine
from sqlalchemy.orm import relationship
from sqlalchemy.orm import sessionmaker, scoped_session


class DBStorage:
    """ database storage engine
    Attributes:
        __engine: sqlalchemy engine
        __session: sqlalchemy session
    """

    __engine = None
    __session = None

    def __init__(self):
        """ creates the engine, fetches variables from env"""
        # db_flavor(mysql, postgress)+db_connector://user:password@host/db_name
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}".format(
                                      getenv("HBNB_MYSQL_USER"),
                                      getenv("HBNB_MYSQL_PWD"),
                                      getenv("HBNB_MYSQL_HOST"),
                                      getenv("HBNB_MYSQL_DB")),
                                      pool_pre_ping=True)
        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """query on the current database session (self.__session) all objects

        Return:
            Dict queried like filestorage
        """

        if cls is None:
            objs = self.__session.query(State).all()
            objs.extend(self.__session.query(City).all())
            objs.extend(self.__session.query(User).all())
            objs.extend(self.__session.query(Place).all())
            objs.extend(self.__session.query(Review).all())
            objs.extend(self.__session.query(Amenity).all())
        else:
            if type(cls) == str:
                cls = eval(cls)
            objs = self.__session.query(cls)
        return {"{}.{}".format(type(obj).__name__, obj.id):\
                obj for obj in objs}

    def new(self, obj):
        """ add the object to the current database session """
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session """
        self.__session.commit()

    def delete(self, obj=None):
        """ delete from the current database session1 """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """ create all tables in the database """
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session  = Session()

    def close(self):
        """ Closes the session"""
        self.__session.close()
