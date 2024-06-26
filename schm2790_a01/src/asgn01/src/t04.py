"""
-------------------------------------------------------
Assignment 1, Task 4
-------------------------------------------------------
Author:  David Brown
ID:      999999999
Email:   dbrown@wlu.ca
__updated__ = "2023-01-29"
-------------------------------------------------------
"""
# Imports
from functions import is_leap_year

CASES = (1900, 1999, 2000, 2004)
for case in CASES:
    actual = is_leap_year(case)
    print(f"is_leap_year({case}): {actual}")
print("Done")
