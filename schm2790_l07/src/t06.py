"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Benjamin Schmid
ID:      169042790
Email:   schm2790@mylaurier.ca
__updated__ = "2023-03-09"
-------------------------------------------------------
"""
# Imports
from List_linked import List

lst = List()

values = [22, 33, 11, 55, 44]
for v in values:
    lst.append(v)

print(lst.reverse_r())
