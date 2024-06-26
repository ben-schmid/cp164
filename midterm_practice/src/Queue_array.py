"""
-------------------------------------------------------
Array version of the Queue ADT.
-------------------------------------------------------
Author:  David Brown
ID:      999999999
Email:   dbrown@wlu.ca
Section: CP164 Spring 2019
__updated__ = "2023-02-23"
-------------------------------------------------------
"""
from copy import deepcopy


class Queue:

    def __init__(self):
        """
        -------------------------------------------------------
        Initializes an empty queue. Data is stored in a Python list.
        Use: queue = Queue()
        -------------------------------------------------------
        Returns:
            a new Queue object (Queue)
        -------------------------------------------------------
        """
        self._values = []

    def __len__(self):
        """
        -------------------------------------------------------
        Returns the length of the queue.
        Use: n = len(queue)
        -------------------------------------------------------
        Returns:
            the number of values in queue.
        -------------------------------------------------------
        """
        # Your code here

        return len(self._values)

    def combine(self, source1, source2):
        """
        -------------------------------------------------------
        Combines two source queues into the current target queue. 
        When finished, the contents of source1 and source2 are interlaced 
        into target and source1 and source2 are empty.
        Order of source values is preserved.
        (iterative algorithm)
        Use: target.combine(source1, source2)
        -------------------------------------------------------
        Parameters:
            source1 - an array-based queue (Queue)
            source2 - an array-based queue (Queue)
        Returns:
            None
        -------------------------------------------------------
        """
        # Your code here
        while len(source1) > 0 and len(source2) > 0:
            self._values.append(source1._values.pop(0))
            self._values.append(source2._values.pop(0))

        while len(source1) > 0:
            self._values.append(source1._values.pop(0))

        while len(source2) > 0:
            self._values.append(source2._values.pop(0))

        return

    def insert(self, value):
        """
        -------------------------------------------------------
        Adds a copy of value to the rear of the queue.
        Use: queue.insert(value)
        -------------------------------------------------------
        Parameters:
            value - a data element (?)
        Returns:
            None
        -------------------------------------------------------
        """
        # Your code here
        self._values.append(deepcopy(value))
        return

    def is_empty(self):
        """
        -------------------------------------------------------
        Determines if the queue is empty.
        Use: b = queue.is_empty()
        -------------------------------------------------------
        Returns:
            True if queue is empty, False otherwise.
        -------------------------------------------------------
        """
        # Your code here

        return len(self._values) == 0

    def is_full(self):
        """
        -------------------------------------------------------
        Determines if the queue is full. (Given the expandable nature
        of the Python list _values, the queue is never full.)
        Use: b = queue.is_full()
        -------------------------------------------------------
        Returns:
            True if queue is full, False otherwise.
        -------------------------------------------------------
        """
        # Your code here

        return False

    def __eq__(self, target):
        """
        ----------------
        Determines whether two Queues are equal.
        Values in self and target are compared and if all values are equal
        and in the same order, returns True, otherwise returns False.
        Use: equals = source == target
        ---------------
        Parameters:
            target - a queue (Queue)
        Returns:
            equals - True if source contains the same values
                as target in the same order, otherwise False. (boolean)
        ---------------
        """
        # Your code here
        equals = False
        if len(self._values) == len(target._values):
            i = 0
            equals = True
            while i < len(self._values) and equals is True:
                if self._values[i] != target._values[i]:
                    equals = False
                i += 1

        return equals

    def peek(self):
        """
        -------------------------------------------------------
        Peeks at the front of queue.
        Use: value = queue.peek()
        -------------------------------------------------------
        Returns:
            value - a copy of the value at the front of queue -
            the value is not removed from queue (?)
        -------------------------------------------------------
        """
        assert (len(self._values) > 0), 'Cannot peek at an empty queue'

        # Your code here
        value = deepcopy(self._values[0])
        return value

    def remove(self):
        """
        -------------------------------------------------------
        Removes and returns value from the queue.
        Use: value = queue.remove()
        -------------------------------------------------------
        Returns:
            value - the value at the front of the queue - the value is
            removed from queue (?)
        -------------------------------------------------------
        """
        assert (len(self._values) > 0), 'Cannot remove from an empty queue'

        # Your code here
        value = self._values.pop(0)

        return value

    def split_alt(self):
        """
        -------------------------------------------------------
        Splits the source queue into separate target queues with values
        alternating into the targets. At finish source queue is empty.
        Order of source values is preserved.
        (iterative algorithm)
        Use: target1, target2 = source.split_alt()
        -------------------------------------------------------
        Returns:
            target1 - contains alternating values from source (Queue)
            target2 - contains remaining values from source (Queue)
        -------------------------------------------------------
        """
        # Your code here
        target1 = Queue()
        target2 = Queue()
        left = True

        while len(self._values) > 0:
            if left:
                target1._values.append(self._values.pop(0))
            else:
                target2._values.append(self._values.pop(0))
            left = not left

        return target1, target2

    def __iter__(self):
        """
        FOR TESTING ONLY
        -------------------------------------------------------
        Generates a Python iterator. Iterates through the queue
        from front to rear.
        Use: for value in queue:
        -------------------------------------------------------
        Returns:
            value - the next value in the queue (?)
        -------------------------------------------------------
        """
        for value in self._values:
            yield value
