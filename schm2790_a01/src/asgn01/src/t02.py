"""
-------------------------------------------------------
Assignment 1, Task 2
-------------------------------------------------------
Author:  David Brown
ID:      999999999
Email:   dbrown@wlu.ca
__updated__ = "2023-01-29"
-------------------------------------------------------
"""
# Imports
from functions import file_analyze

filename = "pelee.txt"
fv = open(filename, "r", encoding="utf-8")
actual = file_analyze(fv)
fv.close()
print(f'filename = "{filename}"')
print('fv = open(filename, "r", encoding="utf-8")')
print(f"file_analyze(fv): {actual}")
print("Done")
