"""
-------------------------------------------------------
Assignment 6, Task 3
-------------------------------------------------------
Author:  David Brown
ID:      999999999
Email:   dbrown@wlu.ca
__updated__ = "2021-11-09"
-------------------------------------------------------
"""
# Imports
from Deque_linked import Deque

# Constants
SEP = '-' * 60


def array_to_deque(deque, source):
    """
    -------------------------------------------------------
    Inserts the contents of source into deque. The contents
    of source are moved into deque, source is empty.
    Use: array_to_deque(deque, source)
    -------------------------------------------------------
    Parameters:
        deque - source Deque (Deque)
        source - source Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    while len(source) > 0:
        deque.insert_front(source.pop(0))
    return


def deque_to_array(deque, target):
    """
    -------------------------------------------------------
    Removes contents of deque into target. Contents of deque
    are moved into target, deque is empty.
    -------------------------------------------------------
    Parameters:
        deque - target Deque (Deque)
        target - target Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    while not deque.is_empty():
        target.append(deque.remove_front())
    return


def deque_test(source):
    """
    -------------------------------------------------------
    Tests deque implementation. the methods of Deque are tested
    for both empty and non-empty deques using the data in source.
    Use: deque_test(source)
    -------------------------------------------------------
    Parameters:
        source - list of data (list of ?)
    Returns:
        None
    -------------------------------------------------------
    """
    deque = Deque()

    print("Deque Initialised")
    print()
    print(SEP)
    print(f"Deque empty (expect True): {deque.is_empty()}")
    print(f"Deque size (expect 0): {len(deque)}")
    print(SEP)
    print("Add one item to Deque")
    deque.insert_front(source[0])
    print("Front of Deque (peek):")
    print(deque.peek_front())
    print(SEP)
    print(f"Deque empty (expect False): {deque.is_empty()}")
    print(f"Deque size (expect 1): {len(deque)}")
    print(SEP)
    print("Deque remove")
    v = deque.remove_front()
    print(v)
    print(SEP)
    print(f"Deque empty (expect True): {deque.is_empty()}")
    print(f"Deque size (expect 0): {len(deque)}")
    print(SEP)
    print("Copy all data to Deque")
    array_to_deque(deque, source)
    print(f"Deque empty (expect False): {deque.is_empty()}")
    print(f"Deque size (expect > 0): {len(deque)}")
    print(SEP)
    print("Front of Deque (peek):")
    print(deque.peek_front())
    print(SEP)
    print("Rear of Deque (peek):")
    print(deque.peek_rear())
    print(SEP)
    print("Remove all elements from Deque")

    while not deque.is_empty():
        v = deque.remove_front()
        print(v)

    print(SEP)
    print(f"Deque empty (expect True): {deque.is_empty()}")
    print(f"Deque size (expect 0): {len(deque)}")
    print()
    return


numbers = list(range(5))
print("Numbers:")
print()
print("Deque Test")
deque_test(numbers)
print("Done")
