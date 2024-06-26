"""
-------------------------------------------------------
Assignment 1, Task 9
-------------------------------------------------------
Author:  David Brown
ID:      999999999
Email:   dbrown@wlu.ca
__updated__ = "2023-01-29"
-------------------------------------------------------
"""
# Imports
from functions import shift

filename = "pelee.txt"
fv = open(filename, "r", encoding="utf-8")
n = 12
print(f'filename = "{filename}"')
print('fv = open(filename, "r", encoding="utf-8")')
print()

for line in fv:
    actual = shift(line.strip(), n)
    print(f'shift("{line.strip()}", {n}):\n       {actual}')
fv.close()
print()
print("Done")
