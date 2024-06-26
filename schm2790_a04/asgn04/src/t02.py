"""
-------------------------------------------------------
Assignment 4 Task 2
-------------------------------------------------------
Author:  David Brown
ID:      999999999
Email:   dbrown@wlu.ca
__updated__ = "2023-02-21"
-------------------------------------------------------
"""
# pylint: disable=protected-access

from Queue_array import Queue

CASES = (
    ([], []),
    ((1, 2, 3), (1, 2, 3)),
    ((1, 2, 3), (3, 2, 1)),
    ((1, 2, 3), (1, 2))
)

q1 = Queue()
q2 = Queue()

for case in CASES:
    q1._values = case[0]
    q2._values = case[1]
    equals = q1 == q2
    print(f"q1: {case[0]}, q2: {case[1]}")
    print(f"q1 == q2: {equals}")
