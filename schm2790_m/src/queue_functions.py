"""
-------------------------------------------------------
Midterm Queue Functions
-------------------------------------------------------
Author: Benjamin Schmid
ID:     169042790
Email:  schm2790@mylaurier.ca
__updated__ = "2023-04-16"
-------------------------------------------------------
"""
from Queue_array import Queue


def queue_rotate(source, n):
    """
    -------------------------------------------------------
    Rotates position of values in source. When finished, values
    in source are rotated n positions to the right.
    Use: queue_rotate(source, n)
    -------------------------------------------------------
    Parameters:
        source - the Queue to rotate (Queue)
        n - amount to rotate Queue values (int)
    Returns‌​‌​​​​‌​​‌‌​‌‌​​​‌‌​‌‌​​‌‌​:
        None
    -------------------------------------------------------
    """

    # Your code here
    n = abs(n)
    for i in range(n):
        source.insert(source.remove())

    return
