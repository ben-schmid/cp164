"""
-------------------------------------------------------
Assignment 4, Task 4
-------------------------------------------------------
Author:  David Brown
ID:      999999999
Email:   dbrown@wlu.ca
__updated__ = "2023-02-21"
-------------------------------------------------------
"""
# Imports
from Queue_array import Queue
from functions import queue_combine

# Constants
SIZE = 12
SEP = "-" * 40


def print_data(d):
    print([v for v in d])
    return


def test_queue_combine():
    # Constants
    A1 = [5, 8, 12, 8]
    A2 = [7, 9, 14]

    print("Testing 'queue_combine'")
    print()

    source1 = Queue()
    source2 = Queue()

    for v in A1:
        source1.insert(v)

    for v in A2:
        source2.insert(v)

    print("Contents of source1:")
    print_data(source1)
    print("Contents of source2:")
    print_data(source2)
    print(SEP)
    print("Combing source1 and source2 into target")
    print()
    target = queue_combine(source1, source2)

    print("Contents of target:")

    print_data(target)
    print()

    print("Testing 'Queue.combine'")
    print()

    source1 = Queue()
    source2 = Queue()

    for v in A1:
        source1.insert(v)

    for v in A2:
        source2.insert(v)

    print("Contents of source1:")
    print_data(source1)
    print("Contents of source2:")
    print_data(source2)
    print(SEP)
    print("Combing source1 and source2 into target")
    print()
    target = Queue()
    target.combine(source1, source2)

    print("Contents of target:")
    print_data(target)
    print()
    print("Done")
    print()


test_queue_combine()
