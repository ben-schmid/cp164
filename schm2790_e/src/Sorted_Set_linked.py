"""
-------------------------------------------------------
Linked version of the Sorted_Set ADT.
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

# Imports
from copy import deepcopy


class _Set_Node:

    def __init__(self, value, next_):
        """
        -------------------------------------------------------
        Initializes a Sorted_Set node that contains a copy of value
        and a link to another Sorted_Set node.
        Use: node = _Set_Node(value, _next)
        -------------------------------------------------------
        Parameters:
            value - value for node (*)
            next_ - another Sorted_Set node (_Set_Node)
        Returns‌​‌​​​​‌​​‌‌​‌‌​​​‌‌​‌‌​​‌‌​:
            a new _Set_Node object (_Set_Node)
        -------------------------------------------------------
        """
        self._value = deepcopy(value)
        self._next = next_


class Sorted_Set:

    def __init__(self):
        """
        -------------------------------------------------------
        Initializes an empty Sorted_Set.
        Use: source = Sorted_Set()
        -------------------------------------------------------
        Returns‌​‌​​​​‌​​‌‌​‌‌​​​‌‌​‌‌​​‌‌​:
            A new linked Sorted_Set object (Sorted_Set)
        -------------------------------------------------------
        """
        self._front = None
        self._rear = None
        self._count = 0

    # ---------------------------------------------------------
    # Helper Methods

    def _append(self, value):
        """
        ---------------------------------------------------------
        Adds a copy of value to the rear of self.
        Private helper method.
        Use: self._append(value)
        -------------------------------------------------------
        Parameters:
            value - data (*)
        Returns‌​‌​​​​‌​​‌‌​‌‌​​​‌‌​‌‌​​‌‌​:
            None
        -------------------------------------------------------
        """

        # your code here
        node = _Set_Node(value, None)
        if self._front is None:
            self._front = node
        else:
            self._rear._next = node
        self._rear = node
        self._count += 1

        return

    def _linear_search(self, key):
        """
        -------------------------------------------------------
        Searches for the occurrence of key in self.
        Private helper method.
        Use: prev, curr, index = self._linear_search(key)
        -------------------------------------------------------
        Parameters:
            key - a partial data value (*)
        Returns‌​‌​​​​‌​​‌‌​‌‌​​​‌‌​‌‌​​‌‌​:
            prev - pointer to node prev to node containing key (_Set_Node)
            curr - pointer to node containing key (_Set_Node)
            index - index of key in self (int)
        -------------------------------------------------------
        """

        prev = None
        curr = self._front
        index = 0

        while curr is not None and curr._value != key:

            prev = curr
            curr = curr._next
            index += 1

        if curr is None:
            index = -1
        return prev, curr, index

    # ---------------------------------------------------------
    # Magic Methods

    def __len__(self):
        """
        -------------------------------------------------------
        Returns the number of values in source.
        Use: n = len(source)
        -------------------------------------------------------
        Returns‌​‌​​​​‌​​‌‌​‌‌​​​‌‌​‌‌​​‌‌​:
            the number of values in source (int)
        -------------------------------------------------------
        """

        # your code here

        return self._count

    def __contains__(self, key):
        """
        ---------------------------------------------------------
        Determines if source contains key.
        Use: contains = key in source
        -------------------------------------------------------
        Parameters:
            key - a partial data value (*)
        Returns‌​‌​​​​‌​​‌‌​‌‌​​​‌‌​‌‌​​‌‌​:
            True if source contains key, False otherwise. (bool)
        -------------------------------------------------------
        """

        _, curr, _ = self._linear_search(key)

        return curr is not None

    def __eq__(self, target):
        """
        -------------------------------------------------------
        Determines whether two Sorted_Sets are equal.
        Values in self and target are compared and if all values are equal
        and in the same order, returns True, otherwise returns False.
        Use: equals = source == target
        -------------------------------------------------------
        Parameters:
            target - a sorted set (Sorted_Set)
        Returns‌​‌​​​​‌​​‌‌​‌‌​​​‌‌​‌‌​​‌‌​:
            equals - True if source contains the same values
                as target in the same order, otherwise False. (boolean)
        -------------------------------------------------------
        Examples:
            {1,2,3} == {1,2,3}: True
            {1,2,3} == {1,2,4}: False
            {1,2,3} == {1,2,3,4}: False
        -------------------------------------------------------
        """

        # your code here
        if self._count != target._count:
            equals = False
        else:
            source_node = self._front
            target_node = target._front

            while source_node is not None and source_node._value == target_node._value:
                source_node = source_node._next
                target_node = target_node._next

            equals = source_node is None
        return equals

    # ---------------------------------------------------------
    # Set Manipulation Methods

    def is_empty(self):
        """
        -------------------------------------------------------
        Determines if source is empty.
        Use: empty = source.is_empty()
        -------------------------------------------------------
        Returns‌​‌​​​​‌​​‌‌​‌‌​​​‌‌​‌‌​​‌‌​:
            True if source is empty, False otherwise. (bool)
        -------------------------------------------------------
        """

        # your code here

        return self._front is None

    def find(self, key):
        """
        -------------------------------------------------------
        Finds and returns a copy of value in source that matches key.
        Use: value = source.find(key)
        -------------------------------------------------------
        Parameters:
            key - a partial data value (*)
        Returns‌​‌​​​​‌​​‌‌​‌‌​​​‌‌​‌‌​​‌‌​:
            value - a copy of the full value matching key, otherwise None (*)
        -------------------------------------------------------
        """

        _, curr, _ = self._linear_search(key)
        if curr is None:
            value = None
        else:
            value = deepcopy(curr._value)

        return value

    def add(self, value):
        """
        ---------------------------------------------------------
        Adds value to source, allows only one copy of value.
        Contents of source remain sorted.
        Use: added = source.add(value)
        -------------------------------------------------------
        Parameters:
            value - a comparable data value (*)
        Returns‌​‌​​​​‌​​‌‌​‌‌​​​‌‌​‌‌​​‌‌​:
            added - True if value is added to source, False otherwise (boolean)
        -------------------------------------------------------
        """
        added = False

        if self._front is None:
            # list is empty, put value in the front
            node = _Set_Node(value, None)
            self._front = node
            self._rear = node
            added = True

        elif value < self._front._value:
            # value front of the list is less than insertion value
            self._front = _Set_Node(value, self._front)
            added = True

        elif value > self._rear._value:
            # rear is less than value added, add value to end of list
            node = _Set_Node(value, None)
            self._rear._next = node
            self._rear = node
            added = True
        else:
            current = self._front
            previous = None
            while value > current._value:
                # loop through nodes of list to find where value goes
                previous = current
                current = current._next
            if value != current._value:
                previous._next = _Set_Node(value, current)
                added = True

        self._count += 1

        return added

    def discard(self, key):
        """
        -------------------------------------------------------
        Finds, removes, and returns the value in source that matches key.
        Returns None if no matching value.
        Use: value = source.discard(key)
        -------------------------------------------------------
        Parameters:
            key - a partial data value (*)
        Returns‌​‌​​​​‌​​‌‌​‌‌​​​‌‌​‌‌​​‌‌​:
            value - the full value matching key, otherwise None (*)
        -------------------------------------------------------
        """

        # your code here

        _, curr, _ = self._linear_search(key)

        return curr

    def clear(self):
        """
        -------------------------------------------------------
        Removes all values from source.
        Use: source.clear()
        -------------------------------------------------------
        Returns‌​‌​​​​‌​​‌‌​‌‌​​​‌‌​‌‌​​‌‌​:
            None
        -------------------------------------------------------
        """

        self._front = None
        self._rear = None
        self._count = 0

        return

    # ---------------------------------------------------------
    # Set Creation Methods

    def difference(self, source2):
        """
        -------------------------------------------------------
        Return a new Sorted_Set with copies of values in source1 that are not in source2.
        Values may appear only once in target. Values must be sorted.
        source1 and source2 are unchanged.
        Use: target = source1.difference(source2)
        -------------------------------------------------------
        Parameters:
            source2 - a linked Sorted_Set. (Sorted_Set)
        Returns‌​‌​​​​‌​​‌‌​‌‌​​​‌‌​‌‌​​‌‌​:
            target - the difference of source1 and source2 (Sorted_Set)
        -------------------------------------------------------
        Examples:
            {1,2,3}.difference({3,4,5}): {1,2}
            {1,2,3,7,9}.difference({3,4,5}): {1,2,7,9}
            {2,3,4}.difference({1,2,3,4,5}): {}
        -------------------------------------------------------
        """

        target = Sorted_Set()
        source_node = source2._front
        self_node = self._front

        while source_node is not None:
            while self_node is not None:
                if self_node._value != source_node._value:
                    target._append(self_node._value)
                self_node = self_node._next
            source_node = source_node._next

        return target

    def isdisjoint(self, target):
        """
        -------------------------------------------------------
        Return True if source has no values in common with target.
        Use: disjoint = source.isdisjoint(target)
        -------------------------------------------------------
        Parameters:
            target - a Sorted_Set to compare against source. (Sorted_Set)
        Returns‌​‌​​​​‌​​‌‌​‌‌​​​‌‌​‌‌​​‌‌​:
            disjoint - True if source has no values in common with target,
                False otherwise. (bool)
        -------------------------------------------------------
        Examples:
            {1,2,3}.isdisjoint({4,5,6,7}): True
            {1,2,3}.isdisjoint({1,4,5,6,7}): False
        -------------------------------------------------------
        """

        # your code here
        target_node = target._front
        self_node = self._front
        disjoint = True

        while target_node is not None and disjoint:
            while self_node is not None and disjoint:
                if self_node._value == target_node._value:
                    disjoint = False
                self_node = self_node._next
            target_node = target_node._next

        return disjoint

    def issuperset(self, target):
        """
        ---------------------------------------------------------
        Test whether every value in target is also in source.
        Use: superset = source.issuperset(target)
        -------------------------------------------------------
        Parameters:
            target - another Sorted_Set. (Sorted_Set)
        Returns‌​‌​​​​‌​​‌‌​‌‌​​​‌‌​‌‌​​‌‌​:
            superset - True if all values in target are also in source,
                False otherwise. (bool)
        -------------------------------------------------------
        Examples:
            {1,2,3}.issuperset({0,1,2,3,4}): False
            {1,2,3,4,5}.issuperset({1,2,4,5}): True
        -------------------------------------------------------
        """
        target_node = target._front
        self_node = self._front
        superset = True

        if self._count != target._count:
            superset = False

        while target_node is not None and self_node is not None and superset:
            if target_node._value != self_node._value:
                superset = False
            self_node = self_node._next
            target_node = target_node._next

        return superset

    def __iter__(self):
        """
        USE FOR TESTING ONLY
        -------------------------------------------------------
        Generates a Python iterator. Iterates through the set
        from first to last items.
        Use: for v in set:
        -------------------------------------------------------
        Returns‌​‌​​​​‌​​‌‌​‌‌​​​‌‌​‌‌​​‌‌​:
            yields
            value - the next value in the set (*)
        -------------------------------------------------------
        """
        curr = self._front

        while curr is not None:
            yield curr._value
            curr = curr._next
