"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Benjamin Schmid
ID:      169042790
Email:   schm2790@mylaurier.ca
__updated__ = "2023-01-20"
-------------------------------------------------------
"""
# Imports
from functions import matrixes_multiply
# Constants
a = [[1, 2, 3],
     [4, 5, 6]]
b = [[7, 8],
     [9, 10],
     [11, 12]]
c = matrixes_multiply(a, b)

print(c)
