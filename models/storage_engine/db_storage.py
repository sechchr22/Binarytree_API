#!/usr/bin/python3
"""
Database engine
"""

from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import BaseModel, Base
from models.binarytree import Binarytree

classes = {"Binarytree": Binarytree}


class DBStorage:
    """
        handles long term storage of all class instances
    """

    __engine = None
    __session = None

    NEWDB_PSQL_USER = 'sech'
    NEWDB_PSQL_PWD = 'gokuaddicte'
    NEWDB_PSQL_HOST = 'localhost'
    NEWDB_PSQL_DB = 'binarytrees'

    def __init__(self):
        """
            creates the engine self.__engine
        """
        self.__engine = create_engine(
            'postgresql://{}:{}@{}/{}'.
            format(DBStorage.NEWDB_PSQL_USER,
                   DBStorage.NEWDB_PSQL_PWD,
                   DBStorage.NEWDB_PSQL_HOST,
                   DBStorage.NEWDB_PSQL_DB),
            pool_pre_ping=True)

    def all(self, cls=None):
        """
           returns a dictionary of all objects
           if cls is passed returns all objects of that class
        """
        new_dict = {}
        for clss in classes:
            if cls is None or cls is classes[clss] or cls is clss:
                objs = self.__session.query(classes[clss]).all()
                for obj in objs:
                    key = obj.__class__.__name__ + '.' + obj.id
                    new_dict[key] = obj
        return (new_dict)

    def new(self, obj):
        """
            adds objects to current database session
        """
        self.__session.add(obj)

    def save(self):
        """
            commits all changes of current database session
        """
        self.__session.commit()

    def rollback_session(self):
        """
            rollsback a session in the event of an exception
        """
        self.__session.rollback()

    def delete(self, obj=None):
        """
            deletes obj from current database session if not None
        """
        if obj:
            self.__session.delete(obj)
            self.save()

    def delete_all(self, cls=None):
        """
           deletes all stored objects, for testing purposes
        """
        for clss in classes:
            if cls is None or cls is classes[clss] or cls is clss:
                objs = self.__session.query(classes[clss]).all()
            for obj in objs:
                obj.delete()

    def reload(self):
        """
           creates all tables in database & session from engine
        """
        Base.metadata.create_all(self.__engine)
        self.__session = scoped_session(
            sessionmaker(
                bind=self.__engine,
                expire_on_commit=False))

    def close(self):
        """
            calls remove() on private session attribute (self.session)
        """
        self.__session.remove()
