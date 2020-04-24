# BINARYTREE REST_API

Basic RestAPI to handle a Binarytree as a resource.

Core Functionality:
  - To create a binarytree
  - To find the last common ancester of 2 nodes

## Basic Concepts

#### Binarytree

A binary tree is a tree data structure in which each node has at most two children, which are referred to as the left child and the right child.

![](https://www.cdn.geeksforgeeks.org/wp-content/uploads/binary-tree-to-DLL.png)

A Binary Tree node contains following parts.

- Data
- left child
- right child

#### Binarytree module in Python

In Python, a binary tree can be represented in different ways with different data structures(dictionary, list) and class representation for a node. However, binarytree library helps to directly implement a binary tree. It also supports heap and binary search tree(BST). This module does not come pre-installed with Pythons standard utility module. To install it type the below command in the terminal.

```sh
pip install binarytree
```
#### Build a binary tree from a List
We can use build() method to convert a list of values into a binary tree.

Here, a given list contains the nodes of tree such that the element at index i has its left child at index 2*i+1, the right child at index 2*i+2 and parent at (i - 1)//2. The elements at index j for j>len(list)//2 are leaf nodes. None indicates the absence of a node at that index. We can also get the list of nodes back after building a binary tree using values attribute.

Example:
```sh
# Creating binary tree from given list 
from binarytree import build 

nodes =[3, 6, 8, 2, 11, None, 13] 
binary_tree = build(nodes) 

print('Binary tree from list :\n', 
      binary_tree) 
```
Output:
```
Binary tree from list :
    ___3
   /    \
  6      8
 / \      \
2   11     13
```

## Environment

You need the following enviroment to run this API.

Ubuntu 16.04 LTS

- Python 3.4.3 : https://askubuntu.com/questions/849190/python-3-4-on-ubuntu-16-04
- Pip3 : https://askubuntu.com/questions/778052/installing-pip3-for-python3-on-ubuntu-16-04-lts-using-a-proxy
- PostgreSQL : https://www.postgresql.org/download/linux/ubuntu/ 
- SQLAlchemy : https://docs.sqlalchemy.org/en/13/intro.html#installation
- Flask : https://pypi.org/project/Flask/
- Binarytree Python module: https://www.geeksforgeeks.org/binarytree-module-in-python/

#### Create the user and database in PostgreSQL
Login and Connect as Default User
```sh
$ sudo -u postgres psql
```
At the psql command prompt
```sh
CREATE USER sech;
```
Setup password
```sh
ALTER USER sech password 'gokuaddicte';
```
Create database
```sh
CREATE DATABASE binarytrees;
```

## Installation

After having the environment setted up, clone the repository.

```sh
git clone https://github.com/sechchr22/Binarytree_API
```

## RUN

To run the API use the following command from the Binarytree_API folder.
```sh
python3 -m api.v1.app
```
Output:
```sh
* Serving Flask app "app" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
```
##### Note: we will be using Host 0.0.0.0 and Port 5000
## ENDPOINTS

#### GET
- ##### /api/binarytree/v1/status

  Description: To know if API is running ok.
  Example: 
  ```sh
  curl -X GET http://0.0.0.0:5000/api/binarytree/v1/status
  ```
  Output:
  ```sh
  {"status":"OK"}
   ```

- ##### /api/binarytree/v1/trees
  Description: Retrieve the list of all Binarytree objects.
  Example:
  ```sh
  curl -X GET http://0.0.0.0:5000/api/binarytree/v1/trees
  ```
   Output:
   If empty
   ```sh
   []
   ```
   Otherwise
   ```sh
   [{"__class__":"Binarytree","created_at":"2020-04-24T16:44:38.184972","id":"5d6090ad-4d33-4e3a-ab7d-f5c62bed2b78","tree_list":[12,11,3,10,5,2,0,null,null,13,1,14,4,null,8],"updated_at":"2020-04-24T16:44:38.185002"}]
   ```
- ##### /api/binarytree/v1/trees/<tree_id>
  Description: Retrieve a Binarytree object.
  Example:
  ```sh
   curl -X GET http://0.0.0.0:5000/api/binarytree/v1/trees/5d6090ad-4d33-4e3a-ab7d-f5c62bed2b78
   ```
   Output:
   If tree exists
   ```sh
   [{"__class__":"Binarytree","created_at":"2020-04-24T16:44:38.184972","id":"5d6090ad-4d33-4e3a-ab7d-f5c62bed2b78","tree_list":[12,11,3,10,5,2,0,null,null,13,1,14,4,null,8],"updated_at":"2020-04-24T16:44:38.185002"}]
   ```
   If not
   ```sh
   {"error":"tree id Not found"}
   ```
- ##### /api/v1/binarytree/trees/<tree_id>/LCA/node1/node2
  Description: Determine lowest common ancestor of two nodes from a given tree.
  Example:
  Having a tree
  ```sh
   {"__class__":"Binarytree","created_at":"2020-04-24T16:51:01.465281","id":"462de96e-205e-4b5c-82b2-6be984e42b74","tree_list":[1,0,8,null,13,11,12,null,null,3,14,6,null,10,4],"updated_at":"2020-04-24T16:51:01.465349"}
   ```
   
   LowestCommonAncestor(3, 12)
   ```sh
   curl -X GET http://0.0.0.0:5000/api/binarytree/v1/trees/462de96e-205e-4b5c-82b2-6be984e42b74/LCA/3/12
   ```
   
   Output:
   ```sh
   {"LCA":"1"}
   ```
   If tree doesn't exists
   ```sh
   {"error":"tree id Not found"}
   ```
#### POST
- ##### /api/v1/binarytree/trees/
  Description: To create a new Binarytree.
  Example:
  ```sh
  curl -X POST http://0.0.0.0:5000/api/binarytree/v1/trees/
  ```
  Output:
  Representation of the new Binarytree created
  ```sh
  {"__class__":"Binarytree","created_at":"2020-04-24T16:59:21.522538","id":"540ac292-1625-4774-92bd-c1a9a3fb0825","tree_list":[6,4,3,5,1,10,12,13,null,null,null,14,9,8],"updated_at":"2020-04-24T16:59:21.522594"}
   ```
#### DELETE
- ##### /api/v1/binarytree/trees/<tree_id>
  Description: Delete a Binarytree object.
  Example:
  ```sh
  curl -X DELETE http://0.0.0.0:5000/api/binarytree/v1/trees/540ac292-1625-4774-92bd-c1a9a3fb0825
  ```
  Output:
  If tree exists
  ```sh
  {"delete":"successful"}
  ```
  If not
   If tree doesn't exists
   ```sh
   {"error":"tree id Not found"}
   ```
## FILE STRUCTURE

### Folder: modules
| File | Description |
| ------ | ------ |
| LCA.py | LowestCommonAncestor Module |
| print_binarytree.py | Print a binarytree from a given list |

### Folder: models
| File | Description |
| ------ | ------ |
| base_model.py | This class defines all common attributes/methods for other classes |
| binarytree.py | Class to define a Binarytree |
#### Subfolder: storage_engine
| File | Description |
| ------ | ------ |
| db_storage.py | Database engine |

### Folder: api
#### Subfolder: v1
| File | Description |
| ------ | ------ |
| app.py | Flask app module |
#### Subfolder: views (inside v1)
| File | Description |
| ------ | ------ |
| index.py | Flask app Index |
| binarytree.py | Binarytree Flask app view module |

# Development
Sergio Andrés Rueda Castro
Backend engineer

##### Contact me:
https://www.linkedin.com/in/sergio-rueda-backend-dev/
https://twitter.com/sechchr


License
----
**Free Software, Hell Yeah!**

