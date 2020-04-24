#!/usr/bin/python3
'''
Module to find the lowest common ancester (LCA) 
of 2 nodes in a Binarytree
'''

def findpath(root, path, v):
    '''
    Function to determine the path from a given
    root node to another node if exists.

    root: root node from a binarytree [BINARYTREE INSTANCE]
    path: list where the path will be stored [LIST]
    v: node value [INT]

    RETURN
    False: if path doesn't exists
    True: if path exists
    ''' 

    if root is None:
        return False
   
    path.append(root.value) 
  
    if root.value == v:
        return True
  
    if ((root.left != None and findpath(root.left, path, v)) or
            (root.right!= None and findpath(root.right, path, v))): 
        return True
     
    path.pop() 
    return False

def LCA(path1, path2):
    '''
    Find LCA of 2 nodes with their paths

    path1: path from root node to node1 [LIST]
    paht2: path from root node to node2 [LIST]
    
    RETURN
    Value of the Last common ancester
    '''

    i = 0

    while (i < len(path1) and i < len(path2)):

        if path1[i] != path2[i]:
            print (i)
            return (path1[i - 1])

        i += 1
    return (path1[i - 2])
