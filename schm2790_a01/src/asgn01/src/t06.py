"""
-------------------------------------------------------
Assignment 1, Task 6
-------------------------------------------------------
Author:  David Brown
ID:      999999999
Email:   dbrown@wlu.ca
__updated__ = "2023-01-29"
-------------------------------------------------------
"""
# Imports
from functions import matrix_transpose

CASES = (
    [[0]],
    [[10]],
    [[1, 1], [1, 1]],
    [[1, 1, 1, 1], [1, 1, 1, 1]],
    [[1, 1], [1, 1], [1, 1], [1, 1]],
    [[0, 1], [2, 3], [4, 5], [6, 7], [8, 9]],
    [[4, 5, 6], [3, 2, 1], [9, 8, 7]]
)
for case in CASES:
    actual = matrix_transpose(case)
    print(f"matrix_transpose({case}): {actual}")
print("Done")
