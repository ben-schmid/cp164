"""
-------------------------------------------------------
Assignment 6, Task 1
-------------------------------------------------------
Author:  David Brown
ID:      999999999
Email:   dbrown@wlu.ca
__updated__ = "2021-11-09"
-------------------------------------------------------
"""
# Imports
from Queue_linked import Queue

# Constants
SEP = '-' * 60


def array_to_queue(queue, source):
    """
    -------------------------------------------------------
    Inserts the contents of source into queue. The contents of source are
    moved into queue, source is empty.
    Use: array_to_queue(queue, source)
    -------------------------------------------------------
    Parameters:
        queue - target Queue (Queue)
        source - source Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    while len(source) > 0:
        queue.insert(source.pop(0))
    return


def queue_to_array(queue, target):
    """
    -------------------------------------------------------
    Removes contents of queue into target. Contents of queue are
    moved into target, queue is empty.
    Use: queue_to_array(queue, target)
    -------------------------------------------------------
    Parameters:
        queue - source Queue (Queue)
        target - target Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    while not queue.is_empty():
        target.append(queue.remove())
    return


def queue_test(source):
    """
    -------------------------------------------------------
    Tests Queue implementation. The methods of Queue are tested
    for both empty and non-empty queues using the data in source.
    Use: queue_test(source)
    -------------------------------------------------------
    Parameters:
        source - list of data (list of ?)
    Returns:
        None
    -------------------------------------------------------
    """
    queue = Queue()

    print("Queue Initialised")
    print()
    print(SEP)
    print(f"Queue empty (expect True): {queue.is_empty()}")
    print(f"Queue size (expect 0): {len(queue)}")
    print(SEP)
    print("Add one item to Queue")
    queue.insert(source[0])
    print("Front of Queue (peek):")
    print(queue.peek())
    print(SEP)
    print(f"Queue empty (expect False): {queue.is_empty()}")
    print(f"Queue size (expect 1): {len(queue)}")
    print(SEP)
    print("Queue remove")
    v = queue.remove()
    print(v)
    print(SEP)
    print(f"Queue empty (expect True): {queue.is_empty()}")
    print(f"Queue size (expect 0): {len(queue)}")
    print(SEP)
    print("Copy all data to Queue")
    array_to_queue(queue, source)
    print(f"Queue empty (expect False): {queue.is_empty()}")
    print(f"Queue size (expect > 0): {len(queue)}")
    print(SEP)
    print("Front of Queue (peek):")
    print(queue.peek())
    print(SEP)
    print("Remove all elements from Queue")

    while not queue.is_empty():
        v = queue.remove()
        print(v)

    print(SEP)
    print(f"Queue empty (expect True): {queue.is_empty()}")
    print(f"Queue size (expect 0): {len(queue)}")
    print()
    return


numbers = list(range(5))
print("Numbers:")
print()
print("Queue Test")
queue_test(numbers)
print("Done")
