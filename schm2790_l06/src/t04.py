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
# Constants

lst = List()
lst.append(5)
print(lst.find(5))
print(lst.index(5))
print(lst.__contains__(5))
lst.append(8)
print(lst.max())
print(lst.min())
