"""
-------------------------------------------------------
Assignment 1, Task 7
-------------------------------------------------------
Author:  David Brown
ID:      999999999
Email:   dbrown@wlu.ca
__updated__ = "2023-01-29"
-------------------------------------------------------
"""
# Imports
from functions import matrixes_multiply

CASES = [
    ([[2]], [[3]]),
    ([[1, 2, 3]], [[4], [5], [6]]),
    ([[1, 2, 3], [4, 5, 6]],
     [[7, 8], [9, 10], [11, 12]])
]
for case in CASES:
    actual = matrixes_multiply(case[0], case[1])
    print(f"matrixes_multiply({case[0]}, {case[1]}): {actual}")
print("Done")
