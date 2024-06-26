"""
-------------------------------------------------------
Assignment 10, Task 1
-------------------------------------------------------
Author:  David Brown
ID:      999999999
Email:   dbrown@wlu.ca
__updated__ = "2022-04-11"
-------------------------------------------------------
"""
# Imports
from random import shuffle

from Sorts_array import Sorts


print("Test Array-Based Radix Sort")
print()
print("Empty list")
a = []
print(a)
Sorts.radix_sort(a)
print(a)
print()
print("Sorted list")
a = list(range(25))
print(a)
Sorts.radix_sort(a)
print(a)
print()
print("Reversed list")
a = list(range(25))
a.reverse()
print(a)
Sorts.radix_sort(a)
print(a)
print()
print("Random list")
a = list(range(25))
shuffle(a)
print(a)
Sorts.radix_sort(a)
print(a)
print()
