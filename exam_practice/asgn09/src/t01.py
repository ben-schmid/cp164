"""
-------------------------------------------------------
Assignment 9, Question 1
-------------------------------------------------------
Author:  David Brown
ID:      999999999
Email:   dbrown@wlu.ca
__updated__ = "2023-04-15"
-------------------------------------------------------
"""
# Imports
from Hash_Set_array import Hash_Set
from functions import insert_words, comparison_total


#FILENAME = "gibbon.txt"
FILENAME = "movies.txt"
FILENAME = "pelee.txt"
hs = Hash_Set(20)
fv = open(FILENAME, "r", encoding="UTF-8")
insert_words(fv, hs)
fv.close()

total, maxword = comparison_total(hs)

print("Using array-based list HashSet")
print()
print(f"Total Comparisons: {total:,d}")
print(
    f"Word with maximum comparisons '{maxword.word}': {maxword.comparisons:,d}")
