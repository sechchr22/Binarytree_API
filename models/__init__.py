#!/usr/bin/python3
"""create a unique DBStorage instance for your application"""

from models.base_model import BaseModel
from models.binarytree import Binarytree
''' from models import all the other resources'''

from models.storage_engine.db_storage import DBStorage
storage = DBStorage()
storage.reload()
