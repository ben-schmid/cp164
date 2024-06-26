"""
-------------------------------------------------------
Assignment 3, Task 2
-------------------------------------------------------
Author:  David Brown
ID:      999999999
Email:   dbrown@wlu.ca
__updated__ = "2023-02-07"
-------------------------------------------------------
"""
# Imports
from Stack_array import Stack
from functions import stack_split_alt

# Constants
SIZE = 6
BASE = 11
RANGE = range(BASE, BASE * SIZE + 1, BASE)
ORDERED = list(RANGE)


def test_stack_split_alt():
    # Constants
    # A1 = [14, 9, 7, 8, 1, 12, 6, 8, 3, 5]
    A1 = [1, 0, 2, 3, 4]

    print("Testing 'stack_split_alt'")
    print()

    source = Stack()
    for v in A1:
        source.push(v)

    print("source contents:")
    for v in source:
        print(v, end=", ")
    print()

    print()
    print("split_alt")
    target1, target2 = stack_split_alt(source)

    print("source contents:")
    for v in source:
        print(v, end=", ")
    print()

    print("target1 contents:")
    for v in target1:
        print(v, end=", ")
    print()

    print("target2 contents:")
    for v in target2:
        print(v, end=", ")
    print()

    print()
    print("Compare to Stack 'split_alt'")
    print()

    source = Stack()
    for v in A1:
        source.push(v)

    print("source contents:")
    for v in source:
        print(v, end=", ")
    print()

    print()
    print("split_alt")
    target1, target2 = source.split_alt()

    print("source contents:")
    for v in source:
        print(v, end=", ")
    print()

    print("target1 contents:")
    for v in target1:
        print(v, end=", ")
    print()

    print("target2 contents:")
    for v in target2:
        print(v, end=", ")
    print()

    print()
    print("Done")


test_stack_split_alt()
