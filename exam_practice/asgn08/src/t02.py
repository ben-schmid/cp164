"""
-------------------------------------------------------
Assignment 8, Question 2
-------------------------------------------------------
Author:  David Brown
ID:      999999999
Email:   dbrown@wlu.ca
__updated__ = "2023-04-12"
-------------------------------------------------------
"""
# Imports
from BST_linked import BST
from Letter import Letter
from functions import do_comparisons, comparison_total, DATA1, DATA2, DATA3


# Constants
SEP = "-" * 30
FILE = "movies.txt"
#FILE = "one_letter.txt"

# initiate 3 BSTs
order_bst = BST()
split_bst = BST()
popular_bst = BST()

# fill them with letter objects
for i in range(len(DATA1)):
    order_bst.insert(Letter(DATA1[i]))
    split_bst.insert(Letter(DATA2[i]))
    popular_bst.insert(Letter(DATA3[i]))


# open file
fv = open(FILE, "r", encoding="UTF-8")

do_comparisons(fv, order_bst)
order_com = comparison_total(order_bst)
do_comparisons(fv, split_bst)
split_com = comparison_total(split_bst)
do_comparisons(fv, popular_bst)
pop_com = comparison_total(popular_bst)

fv.close()

print(f"For '{FILE}':")
print()
print(f"Comparing by order: {DATA1}")
print(f"Total Comparisons: {order_com:,}")
print(SEP)
print(f"Comparing by order: {DATA2}")
print(f"Total Comparisons: {split_com:,}")
print(SEP)
print(f"Comparing by order: {DATA3}")
print(f"Total Comparisons: {pop_com:,}")
