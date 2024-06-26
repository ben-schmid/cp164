"""
-------------------------------------------------------
Simple midterm function testing
-------------------------------------------------------
Author: Benjamin Schmid
ID:     169042790
Email:  schm2790@mylaurier.ca
__updated__ = "2023-04-16"
-------------------------------------------------------
"""
# pylint: disable=protected-access

# Imports
from List_array import List
from Queue_array import Queue
from queue_functions import queue_rotate


# Constants
SEP = "-" * 60
SIZE = 6


def test_queue_rotate():
    print(SEP)
    print("Testing 'queue_rotate'")
    print()
    CASES = (0, SIZE, 1, -1, SIZE // 2,)
    values = [11, 22, 33, 44, 55]

    for case in CASES:
        source = Queue()

        for v in values:
            source.insert(v)
        queue_rotate(source, case)
        print(f"queue_rotate({values}, {case}): {source._values}")
    print()
    return


def test_rotate():
    print(SEP)
    print("Testing 'rotate'")
    print()
    CASES = (0, 8, 1, -1, SIZE // 2,)
    values = [11, 22, 33, 44, 55]

    for case in CASES:
        source = Queue()

        for v in values:
            source.insert(v)
        source.rotate(case)
        print(f"{values}: source.rotate({case}): {source._values}")
    print()
    return


def test_count_pairs():
    print(SEP)
    print("Testing 'count_pairs'")
    print()
    CASES = (
        [],
        [0, 1, 2, 3],
        [0, 0, 1, 1, 2, 2, 3, 3],
        [99, 99, 99, 99, 99]
    )

    for values in CASES:
        source = List()

        for v in values:
            source.append(v)
        pairs = source.count_pairs()
        print(f"{values}: source.count_pairs(): {pairs}")
    print()
    return


if __name__ == "__main__":
    # Main code
    # Add or remove commenting as appropriate
    print("Midterm Testing")
    test_rotate()
    test_queue_rotate()
    test_count_pairs()
