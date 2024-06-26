"""
-------------------------------------------------------
Assignment 3, Task 4
-------------------------------------------------------
Author:  David Brown
ID:      999999999
Email:   dbrown@wlu.ca
__updated__ = "2023-02-07"
-------------------------------------------------------
"""
# Imports
from functions import postfix

CASES = ("0", "4 5 + 12 * 2 3 * -", "12 5 -")
print("Testing 'postfix'")
print()

for string in CASES:
    a = postfix(string)
    print(f"postfix('{string}') -> {a}")
print("Done")
