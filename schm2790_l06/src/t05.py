"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Benjamin Schmid
ID:      169042790
Email:   schm2790@mylaurier.ca
__updated__ = "2023-03-03"
-------------------------------------------------------
"""
# Imports
from List_linked import List

lst = List()

lst.append(5)
lst.append(6)
print(lst.__getitem__(1))
lst.__setitem__(1, 1)
print(lst.__getitem__(1))