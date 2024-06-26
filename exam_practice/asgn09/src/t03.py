"""
-------------------------------------------------------
Assignment 9, Question 3
-------------------------------------------------------
Author:  David Brown
ID:      999999999
Email:   dbrown@wlu.ca
__updated__ = "2023-04-04"
-------------------------------------------------------
"""
# Imports
from Hash_Set_BST import Hash_Set
from functions import insert_words, comparison_total


FILENAME = "miserables.txt"
# FILENAME = "movies.txt"
FILENAME = "otoos610.txt"
FILENAME = "one.txt"
FILENAME = "pelee.txt"
hs = Hash_Set(20)
fv = open(FILENAME, "r", encoding="UTF-8")
insert_words(fv, hs)
fv.close()

total, maxword = comparison_total(hs)

print("Using linked BST HashSet")
print()
print(f"Total Comparisons: {total:,d}")
print(
    f"Word with maximum comparisons '{maxword.word}': {maxword.comparisons:,d}")
