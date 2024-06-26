"""
-------------------------------------------------------
Assignment 4, Task 6
-------------------------------------------------------
Author:  David Brown
ID:      999999999
Email:   dbrown@wlu.ca
__updated__ = "2023-02-21"
-------------------------------------------------------
"""
# Imports
from Priority_Queue_array import Priority_Queue
from functions import pq_split_key

# Constants
SIZE = 8
SEP = "-" * 60


def test_pq_split_key():
    print("Testing 'pq_split_key'")
    print()
    # Put data into source in reverse to show differences between
    # this and Priority_Queue.split_key()
    # a = list(range(SIZE))[::-1]
    a = [4, 1, 7, 3, 9, 2, 4, 5, 1, 7, 0, 9]
    source = Priority_Queue()

    for v in a:
        source.insert(v)

    print("Contents of source:")

    for v in source:
        print(v, end=", ")
    print()
    print(SEP)
    print("Split source into target1 and target2")
    print()
    target1, target2 = pq_split_key(source, 4)
    print("Contents of target1:")

    for v in target1:
        print(v, end=", ")
    print()
    print("Contents of target2:")

    for v in target2:
        print(v, end=", ")
    print()
    print(SEP)
    print("Testing 'Priority_Queue.split_key'")
    print()
    source = Priority_Queue()

    for v in a:
        source.insert(v)

    print("Contents of source:")

    for v in source:
        print(v, end=", ")
    print()
    print(SEP)
    print("Split source into target1 and target2")
    print()
    target1, target2 = source.split_key(4)
    print("Contents of target1:")

    for v in target1:
        print(v, end=", ")
    print()
    print("Contents of target2:")

    for v in target2:
        print(v, end=", ")
    print()
    print()
    print("Done")


test_pq_split_key()
