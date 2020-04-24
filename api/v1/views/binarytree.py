#!/usr/bin/python3
"""
=============================================================================================================
Retrieve the list of all Binarytree objects: GET /api/v1/binarytree/trees
Retrieve a Binarytree object: GET /api/v1/binarytree/trees/<tree_id>
Retrieve lost common ancestor of two nodes: GET /api/v1/binarytree/trees/<tree_id>/LCA/node1/node2

Creates Binarytree object: POST /api/v1/binarytree/trees

Delete Binarytree object: DELETE /api/v1/binarytree/trees/<tree_id>
=============================================================================================================
"""

from api.v1.views import app_views
from models import storage
from flask import jsonify, abort, request, make_response
from models.binarytree import Binarytree
from binarytree import tree, build
from modules.LCA import *


@app_views.route('/trees', strict_slashes=False, methods=['GET'])
def retrieve_trees():
    """ Retrieve the list of all Binarytree objects"""

    tree_list = []
    for key, value in storage.all("Binarytree").items():
        tree_list.append(value.to_dict())
    return jsonify(tree_list)

@app_views.route('/trees/<string:tree_id>', strict_slashes=False,
                 methods=['GET'])
def retrieve_tree_id(tree_id):
    """Method to retrieve an binarytree using the id"""

    key = 'Binarytree.' + tree_id
    if key in storage.all("Binarytree").keys():
        return jsonify(storage.all("Binarytree").get(key).to_dict())
    else:
        abort(404)

@app_views.route('/trees/<string:tree_id>/LCA/<int:node1>/<int:node2>', strict_slashes=False,
                 methods=['GET'])
def retrieve_LCA(tree_id, node1, node2):
    """Method to retrieve Last common ancester of 2 nodes in a Binary tree"""

    key = 'Binarytree.' + tree_id
    if key in storage.all("Binarytree").keys():

        list_rep = storage.all("Binarytree")[key].tree_list
        tree_inst = build(list_rep)

        path1, path2 = [], []

        exist1 = findpath(tree_inst, path1, node1)
        exist2 = findpath(tree_inst, path2, node2)

        if exist1 is False:
            return make_response(jsonify({"error": "Node1 Not found"}), 404)
        
        if exist2 is False:
            return make_response(jsonify({"error": "Node2 Not found"}), 404)

        L_C_A = LCA(path1, path2)
  
        if LCA is not None:
            return make_response(jsonify({"LCA": "{}".format(L_C_A)}), 200)
    else:
        abort(404)

@app_views.route('/trees/<string:tree_id>', methods=['DELETE'],
                 strict_slashes=False)
def del_trees_id(tree_id):
    """Method to delete an user object using the DELETE method and his id"""

    key = 'Binarytree.' + tree_id
    if key in storage.all("Binarytree").keys():
        obj = storage.all("Binarytree")[key]
        storage.delete(obj)
        storage.save()
        return make_response(jsonify({"delete": "successful"}), 200)
    else:
        abort(404)


@app_views.route('/trees/', methods=['POST'], strict_slashes=False)
def post_tree():
    """Method to create a random Binarytree object using POST"""

    new_tree = tree()
    list_rep = new_tree.values

    new_tree_obj = Binarytree()
    new_tree_obj.tree_list = list_rep
    new_tree_obj.save()

    key = 'Binarytree.' + new_tree_obj.id

    return jsonify(storage.all("Binarytree").get(key).to_dict())
