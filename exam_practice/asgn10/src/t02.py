"""
-------------------------------------------------------
Assignment 10, Task 2
-------------------------------------------------------
Author:  David Brown
ID:      999999999
Email:   dbrown@wlu.ca
__updated__ = "2022-04-11"
-------------------------------------------------------
"""
# Imports
from random import shuffle

from List_linked import List
from Sorts_List_linked import Sorts


def array_to_linked(array):
    temp = List()

    for v in array:
        temp.append(v)
    return temp


def linked_to_array(temp):
    array = []

    for v in temp:
        array.append(v)
    return array


print("Test Linked Radix Sort")
print()
print("Empty list")
a = []
print(a)
source = array_to_linked(a)
Sorts.radix_sort(source)
a = Sorts.to_array(source)
print(a)
print()
print("Sorted list")
a = list(range(25))
print(a)
source = array_to_linked(a)
Sorts.radix_sort(source)
a = Sorts.to_array(source)
print(a)
print()
print("Reversed list")
a = list(range(25))
a.reverse()
print(a)
source = array_to_linked(a)
Sorts.radix_sort(source)
a = Sorts.to_array(source)
print(a)
print()
print("Random list")
a = list(range(25))
shuffle(a)
print(a)
source = array_to_linked(a)
Sorts.radix_sort(source)
a = Sorts.to_array(source)
print(a)
print()
