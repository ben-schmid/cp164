"""
-------------------------------------------------------
Assignment 8, Question 1
-------------------------------------------------------
Author:  David Brown
ID:      999999999
Email:   dbrown@wlu.ca
__updated__ = "2023-04-13"
-------------------------------------------------------
"""
# Imports
from BST_linked import BST

# Constants
SEP = "-" * 30
BALANCED = [4, 1, 5, 0, 2, 3, 6]

bst = BST()

for v in BALANCED:
    bst.insert(v)

print(f"Values: {BALANCED}")
print()
print("Preorder")
print(bst.preorder())
print("Inorder:")
print(bst.inorder())
print("Postorder")
print(bst.postorder())
print("Levelorder")
print(bst.levelorder())
print("Minimum")
print(bst.min())
print("Leaf Count")
print(bst.leaf_count())
print("One Child Count")
print(bst.one_child_count())
print("Two Child Count")
print(bst.two_child_count())
print("Is Balanced")
print(bst.is_balanced())
print("Valid")
print(bst.is_valid())
