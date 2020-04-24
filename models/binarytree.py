#!/usr/bin/python3
"""Binarytree class"""

from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer
from sqlalchemy.types import ARRAY


class Binarytree(BaseModel, Base):
    """
    Class to define a Binarytree
    tree_list: represents the serialization of a binarytree
    """

    __tablename__ = 'Binarytrees'
    tree_list = Column(ARRAY(Integer(), dimensions=1), default=[])

    def __init__(self, *args, **kwargs):
        """initializes Binarytree Class"""
        super().__init__(*args, **kwargs)
