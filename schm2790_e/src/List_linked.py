"""
-------------------------------------------------------
Linked version of the list ADT.
-------------------------------------------------------
Author: Benjamin Schmid
ID:     169042790
Email:  schm2790@mylaurier.ca
__updated__ = "2023-04-17"
-------------------------------------------------------
"""
# pylint: disable=W0212
# pylint: disable=E2515
# pylint: disable=E0303
# pylint: disable=W0613
# pylint: disable=E1128

from copy import deepcopy


class List:

    def shift_front(self):
        """
        -------------------------------------------------------
        Moves the front node to the rear of the List.
        Use: source.shift_front()
        -------------------------------------------------------
        Returns‌​‌​​​​‌​​‌‌​‌‌​​​‌‌​‌‌​​‌‌​:
            None
        -------------------------------------------------------
        """

        if self._front is not None and self._front._next is not None:
            node = self._front
            self._front = node._next
            self._rear._next = node
            self._rear = node
            node._next = None

        return

    def shift_rear(self):
        """
        -------------------------------------------------------
        Moves the rear node to the front of the List.
        Use: source.shift_rear()
        -------------------------------------------------------
        Returns‌​‌​​​​‌​​‌‌​‌‌​​​‌‌​‌‌​​‌‌​:
            None
        -------------------------------------------------------
        """

        if self._front is not None and self._front._next is not None:

            # find rear._prev
            node = self._front
            while node._next != self._rear:
                node = node._next

            # Move the rear node to the front
            self._rear._next = self._front
            self._front = self._rear

            # Update the rear and node
            self._rear = node
            node._next = None

        return

    def _remove_front(self):
        """
        -------------------------------------------------------
        Removes the first node in the list and returns its value.
        Use: value = lst.remove_front()
        -------------------------------------------------------
        Returns:
            value - the first value in the list (?)
        -------------------------------------------------------
        """
        assert self._front is not None, "Cannot remove from an empty list"

        value = self._front._value
        self._front = self._front._next
        self._count -= 1

        if self._front is None:
            # Last node has been removed
            self._rear = None
        return value


# DO NOT CHANGE CODE BELOW THIS LINE
# =======================================================================

    def __init__(self):
        """
        -------------------------------------------------------
        Initializes an empty list.
        Use: lst = List()
        -------------------------------------------------------
        Returns‌​‌​​​​‌​​‌‌​‌‌​​​‌‌​‌‌​​‌‌​:
            a new List object (List)
        -------------------------------------------------------
        """
        self._front = None
        self._rear = None
        self._count = 0

    def is_empty(self):
        """
        -------------------------------------------------------
        Determines if the list is empty.
        Use: b = lst.is_empty()
        -------------------------------------------------------
        Returns‌​‌​​​​‌​​‌‌​‌‌​​​‌‌​‌‌​​‌‌​:
            True if the list is empty, False otherwise.
        -------------------------------------------------------
        """
        return self._front is None

    def __len__(self):
        """
        -------------------------------------------------------
        Returns the number of values in the list.
        Use: n = len(lst)
        -------------------------------------------------------
        Returns‌​‌​​​​‌​​‌‌​‌‌​​​‌‌​‌‌​​‌‌​:
            the number of values in the list.
        -------------------------------------------------------
        """
        return self._count

    def append(self, value):
        """
        ---------------------------------------------------------
        Adds a copy of value to the end of the List.
        Use: lst.append(value)
        -------------------------------------------------------
        Parameters:
            value - a data element (?)
        Returns‌​‌​​​​‌​​‌‌​‌‌​​​‌‌​‌‌​​‌‌​:
            None
        -------------------------------------------------------
        """
        # Create the new node.
        node = _List_Node(value, None)

        if self._front is None:
            # list is empty - update the front of the List.
            self._front = node
        else:
            self._rear._next = node
        # Update the rear of the List.
        self._rear = node
        self._count += 1
        return

    def __iter__(self):
        """
        USE FOR TESTING ONLY
        -------------------------------------------------------
        Generates a Python iterator. Iterates through the list
        from front to rear.
        Use: for v in s:
        -------------------------------------------------------
        Returns‌​‌​​​​‌​​‌‌​‌‌​​​‌‌​‌‌​​‌‌​:
            yields
            value - the next value in the list (?)
        -------------------------------------------------------
        """
        current = self._front

        while current is not None:
            yield current._value
            current = current._next


class _List_Node:

    def __init__(self, value, next_):
        """
        -------------------------------------------------------
        Initializes a list node that contains a copy of value
        and a link to the next node in the list.
        Use: node = _List_Node(value, _next)
        -------------------------------------------------------
        Parameters:
            _value - value value for node (?)
            _next - another list node (_List_Node)
        Returns‌​‌​​​​‌​​‌‌​‌‌​​​‌‌​‌‌​​‌‌​:
            a new _List_Node object (_List_Node)
        -------------------------------------------------------
        """
        self._value = deepcopy(value)
        self._next = next_
