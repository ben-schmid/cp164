"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Benjamin Schmid
ID:      169042790
Email:   schm2790@mylaurier.ca
__updated__ = "2023-04-09"
-------------------------------------------------------
"""
# Imports
from Sorts_List_linked import Sorts

a = [10, 1, 3, 12, 0]

Sorts.radix_sort(a)

for v in a:
    print(v)
