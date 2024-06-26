"""
-------------------------------------------------------
Assignment 8, Question 3
-------------------------------------------------------
Author:  David Brown
ID:      999999999
Email:   dbrown@wlu.ca
__updated__ = "2020-03-20"
-------------------------------------------------------
"""
# Imports
from BST_linked import BST
from Letter import Letter
from functions import letter_table, do_comparisons, DATA3


# initiate a BST
FILE = "movies.txt"

pop_bst = BST()

# fill them with letter objects
for i in range(len(DATA3)):
    pop_bst.insert(Letter(DATA3[i]))

fv = open(FILE, "r", encoding="UTF-8")
do_comparisons(fv, pop_bst)
fv.close()
letter_table(pop_bst)
