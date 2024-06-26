"""
-------------------------------------------------------
Assignment 9, Question 4
-------------------------------------------------------
Author:  David Brown
ID:      999999999
Email:   dbrown@wlu.ca
__updated__ = "2021-03-31"
-------------------------------------------------------
"""
# Imports
from BST_linked import BST

# Constants
SEP = '-'
BALANCED = [11, 7, 15, 6, 9, 12, 18, 8]

bst = BST()

for v in BALANCED:
    bst.insert(v)

data = bst.preorder()
print(f"BST data preorder: {data}")
print(SEP)
key = 999
print(f"Attempt to remove invalid key: {key}")
r = bst.remove(key)
print(f"Value removed: {r}")
data = bst.preorder()
print(f"BST data preorder: {data}")
print(SEP)
print("Remove node with one child: 9")
r = bst.remove(9)
print(f"Value removed: {r}")
data = bst.preorder()
print(f"BST data preorder: {data}")
print(SEP)
print("Remove node with no child: 12")
r = bst.remove(12)
print(f"Value removed: {r}")
data = bst.preorder()
print(f"BST data preorder: {data}")
print(SEP)
print("Remove node with two children: 11")
r = bst.remove(11)
print(f"Value removed: {r}")
data = bst.preorder()
print(f"BST data preorder: {data}")
print(SEP)
