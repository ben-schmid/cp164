"""
-------------------------------------------------------
Assignment 6, Task 2
-------------------------------------------------------
Author:  David Brown
ID:      999999999
Email:   dbrown@wlu.ca
__updated__ = "2021-11-09"
-------------------------------------------------------
"""
# Imports
from Priority_Queue_linked import Priority_Queue

# Constants
SEP = '-' * 60


def array_to_pq(pq, source):
    """
    -------------------------------------------------------
    Inserts the contents of source into pq. The contents of
    source are moved into pq, source is empty.
    Use: array_to_pq(pq, source)
    -------------------------------------------------------
    Parameters:
        pq - target Priority_Queue (Priority_Queue)
        source - source Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    while len(source) > 0:
        pq.insert(source.pop(0))
    return


def pq_to_array(pq, target):
    """
    -------------------------------------------------------
    Removes contents of pq into target. Contents of pq are moved
    into target, pq is empty.
    Use: pq_to_array(pq, target)
    -------------------------------------------------------
    Parameters:
        pq - source Priority_Queue object (Priority_Queue)
        target - target Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    while not pq.empty():
        target.append(pq.remove())
    return


def priority_queue_test(source):
    """
    -------------------------------------------------------
    Tests priority queue implementation. the methods of
    Priority_Queue are tested for both empty and
    non-empty priority queues using the data in source
    Use: priority_queue_test(source)
    -------------------------------------------------------
    Parameters:
        source - list of data (list of ?)
    Returns:
        None
    -------------------------------------------------------
    """
    pq = Priority_Queue()

    print("Priority Queue Initialised")
    print()
    print(SEP)
    print(f"Priority Queue empty (expect True): {pq.is_empty()}")
    print(f"Priority Queue size (expect 0): {len(pq)}")
    print(SEP)
    print("Add one item to Priority Queue")
    pq.insert(source[0])
    print("Front of Priority Queue (peek):")
    print(pq.peek())
    print(SEP)
    print(f"Priority Queue empty (expect False): {pq.is_empty()}")
    print(f"Priority Queue size (expect 1): {len(pq)}")
    print(SEP)
    print("Priority Queue remove")
    v = pq.remove()
    print(v)
    print(SEP)
    print(f"Priority Queue empty (expect True): {pq.is_empty()}")
    print(f"Priority Queue size (expect 0): {len(pq)}")
    print(SEP)
    print("Copy all data to Priority Queue")
    array_to_pq(pq, source)
    print(f"Priority Queue empty (expect False): {pq.is_empty()}")
    print(f"Priority Queue size (expect > 0): {len(pq)}")
    print(SEP)
    print("Front of Priority Queue (peek):")
    print(pq.peek())
    print(SEP)
    print("Remove all elements from Priority Queue")

    while not pq.is_empty():
        v = pq.remove()
        print(v)

    print(SEP)
    print(f"Priority Queue empty (expect True): {pq.is_empty()}")
    print(f"Priority Queue size (expect 0): {len(pq)}")
    print()
    return


numbers = list(range(5))
print("Numbers:")
print()
print("Priority Queue Test")
priority_queue_test(numbers)
print("Done")
