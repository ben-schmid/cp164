"""
-------------------------------------------------------
Assignment 1, Task 5
-------------------------------------------------------
Author:  David Brown
ID:      999999999
Email:   dbrown@wlu.ca
__updated__ = "2023-01-29"
-------------------------------------------------------
"""
# Imports
from functions import is_valid

CASES = (
    "",
    "_var",
    "var",
    "2var",
    "var_",
    "var!",
    "_"
)
for case in CASES:
    actual = is_valid(case)
    print(f'is_valid("{case}"): {actual}')
print("Done")
