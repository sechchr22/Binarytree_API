#!/usr/bin/python3
'''
Views package init
'''

from flask import Blueprint
app_views = Blueprint('app_views', __name__, url_prefix='/api/binarytree/v1')

from api.v1.views.index import *
from api.v1.views.binarytree import *
