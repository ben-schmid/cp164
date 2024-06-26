"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Benjamin Schmid
ID:      169042790
Email:   schm2790@mylaurier.ca
__updated__ = "2023-04-01"
-------------------------------------------------------
"""
# Imports
from functions import comparison_total, insert_words
from Hash_Set_array import Hash_Set

h = Hash_Set(20)

fv = open("gibbon.txt", "r")
insert_words(fv, h)


total, max_word = comparison_total(h)

print("Using array-based list Hash_Set")
print()
print(f"Total Comparisons: {total:,d}")
print(
    f"Word with maximum comparisons '{max_word.word}': {max_word.comparisons:,d}")
