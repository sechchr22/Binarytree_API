#!/usr/bin/python3
"""Print binary tree Module"""

from binarytree import build

def print_tree(tree_list):
    """Function to print a binarytree from its serialization"""
    tree = build(tree_list)
    print(tree)
