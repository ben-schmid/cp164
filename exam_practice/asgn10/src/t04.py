"""
-------------------------------------------------------
Assignment 10, Task 4
-------------------------------------------------------
Author:  David Brown
ID:      999999999
Email:   dbrown@wlu.ca
__updated__ = "2022-04-11"
-------------------------------------------------------
"""
# Imports
from random import shuffle

from Deque_linked import Deque
from Sorts_Deque_linked import Sorts


def array_to_linked(array):
    temp = Deque()

    for v in array:
        temp.insert_front(v)
    return temp


def linked_to_array(temp):
    array = []

    for v in temp:
        array.append(v)
    return array


print("Test Linked Gnome Sort")
print()
print("Empty list")
a = []
print(a)
source = array_to_linked(a)
Sorts.gnome_sort(source)
a = linked_to_array(source)
print(a)
print()
print("Sorted list")
a = list(range(25))
print(a)
source = array_to_linked(a)
Sorts.gnome_sort(source)
a = linked_to_array(source)
print(a)
print()
print("Reversed list")
a = list(range(25))
a.reverse()
print(a)
source = array_to_linked(a)
Sorts.gnome_sort(source)
a = linked_to_array(source)
print(a)
print()
print("Random list")
a = list(range(25))
shuffle(a)
print(a)
source = array_to_linked(a)
Sorts.gnome_sort(source)
a = linked_to_array(source)
print(a)
print()
