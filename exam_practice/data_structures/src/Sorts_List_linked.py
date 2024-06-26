"""
-------------------------------------------------------
Linked versions of various sorts. Implemented on linked Lists.
-------------------------------------------------------
Author:  David Brown
ID:      999999999
Email:   dbrown@wlu.ca
__updated__ = "2023-03-30"
-------------------------------------------------------
"""
# pylint: disable=protected-access

# Imports
from math import log10, floor
from List_linked import List


class Sorts:
    """
    -------------------------------------------------------
    Defines a number of linked sort operations.
    Uses class attribute 'swaps' to determine how many times
    elements are swapped by the class.
    Use: print(Sorts.swaps)
    Use: Sorts.swaps = 0
    -------------------------------------------------------
    """
    swaps = 0  # Tracks swaps performed.

    # The Sorts

    @staticmethod
    def radix_sort(a):
        """
        -------------------------------------------------------
        Performs a base 10 radix sort.
        Use: radix_sort(a)
        -------------------------------------------------------
        Parameters:
            a - a List of base 10 integers (List)
        Returns:
            None
        -------------------------------------------------------
        """
        if len(a) > 0:
            # Determine the maximum digit in the numbers in a.
            max_val = a.max()
            passes = floor(log10(max_val, 10) + 1)
            # Create the is_empty buckets.
            buckets = []

            for _ in range(10):
                buckets.append(List())

            for digit in range(passes):
                # Calculate the digit extraction numerator and denominator.
                d = 10 ** digit
                n = d * 10

                while not a.is_empty():
                    # Extract the individual digit.
                    index = a._front._value % n // d
                    # Move front node of a to rear of proper bucket.
                    buckets[index]._move_front_to_rear(a)

                for bucket in buckets:
                    # Concatenate the buckets back into a from left to right.
                    if bucket._front is not None:
                        a._append_list(bucket)
        return

    # Sort Utilities

    @staticmethod
    def to_array(a):
        """
        -------------------------------------------------------
        Copies list values to a Python list.
        Use: values = to_array(a)
        -------------------------------------------------------
        Parameters:
            a - a linked list of comparable elements (?)
        Returns:
            values - the contents of a in a Python list.= (list of ?)
        -------------------------------------------------------
        """
        values = []
        curr = a._front

        while curr is not None:
            values.append(curr._value)
            curr = curr._next
        return values

    @staticmethod
    def is_sorted(a):
        """
        -------------------------------------------------------
        Determines whether an array is sorted or not.
        Use: srtd = Sorts.is_sorted(a)
        -------------------------------------------------------
        Parameters:
            a - an array of comparable elements (?)
        Returns:
            srtd - True if contents of a are sorted,
                False otherwise (boolean)
       -------------------------------------------------------
        """
        srtd = True
        curr = a._front

        while srtd and curr is not None and \
                curr._next is not None:

            if curr._value <= curr._next._value:
                curr = curr._next
            else:
                srtd = False
        return srtd
