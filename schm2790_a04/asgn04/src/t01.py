"""
-------------------------------------------------------
Assignment 4, Task 1
-------------------------------------------------------
Author:  David Brown
ID:      999999999
Email:   dbrown@wlu.ca
__updated__ = "2023-02-21"
-------------------------------------------------------
"""
# Imports
from Queue_circular import Queue
from utilities import array_to_queue


# Constants
SIZE = 10
SEP = "-" * 40


def queue_test(source):
    """
    -------------------------------------------------------
    Tests queue implementation.
    Use: test_Queue_array(source)
    -------------------------------------------------------
    Parameters:
        source - list of data (list of ?)
    Returns:
        the methods of CircularQueue are tested for both is_empty and
        non-is_empty queues using the data in source:
        is_empty, push, pop, peek
    -------------------------------------------------------
    """
    q = Queue()

    print("Queue Initialised")
    print()
    print(SEP)
    print(f"Queue is_empty (expect True): {q.is_empty()}")
    print(f"Queue size (expect 0): {len(q)}")
    print(SEP)
    print("Add one item to Queue")
    q.insert(source[0])
    print("Front of Queue (peek):")
    print(q.peek())
    print(SEP)
    print(f"Queue is_empty (expect False): {q.is_empty()}")
    print(f"Queue size (expect 1): {len(q)}")
    print(SEP)
    print("Queue remove")
    v = q.remove()
    print(v)
    print(SEP)
    print(f"Queue is_empty (expect True): {q.is_empty()}")
    print(f"Queue size (expect 0): {len(q)}")
    print(SEP)
    print("Copy all data to Queue")
    array_to_queue(q, source)
    print(f"Queue is_empty (expect False): {q.is_empty()}")
    print(f"Queue size (expect > 0): {len(q)}")
    print(SEP)
    print("Front of Queue (peek):")
    print(q.peek())
    print(SEP)
    print("Remove all elements from Queue")

    while not q.is_empty():
        v = q.remove()
        print(v, end=", ")
    print()

    print(SEP)
    print(f"Queue is_empty (expect True): {q.is_empty()}")
    print(f"Queue size (expect 0): {len(q)}")
    print()
    return


a = list(range(SIZE))
queue_test(a)
