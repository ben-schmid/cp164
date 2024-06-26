"""
-------------------------------------------------------
Assignment 1, Task 1
-------------------------------------------------------
Author:  David Brown
ID:      999999999
Email:   dbrown@wlu.ca
__updated__ = "2023-01-27"
-------------------------------------------------------
"""
# Imports
from copy import copy
from functions import clean_list

CASES = (
    [],
    list(range(6)),
    [0] * 6,
    list(range(4)) * 3
)
for case in CASES:
    result = copy(case)
    clean_list(result)
    print(f"clean_list({case})")
    print(f"  Updated list: {result}")
print("Done")
