"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Benjamin Schmid
ID:      169042790
Email:   schm2790@mylaurier.ca
__updated__ = "2023-03-24"
-------------------------------------------------------
"""
# Imports
from Hash_Set_array import Hash_Set

h = Hash_Set(10)

for i in range(10):
    h.insert("as")
    h.insert("we")
    h.insert("pooo")
    h.insert("pee")
h.debug()
