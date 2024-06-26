"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Benjamin Schmid
ID:      169042790
Email:   schm2790@mylaurier.ca
__updated__ = "2023-03-04"
-------------------------------------------------------
"""
# Imports
from Queue_array import Queue
from Priority_Queue_array import Priority_Queue
from Stack_array import Stack
# Constants
OPERATORS = "+-*/"


def queue_combine(source1, source2):
    """
    -------------------------------------------------------
    Combines two source queues into the current target queue.
    When finished, the contents of source1 and source2 are interlaced
    into target and source1 and source2 are empty.
    Order of source values is preserved.
    (iterative algorithm)
    Use: target = queue_combine(source1, source2)
    -------------------------------------------------------
    Parameters:
        source1 - a queue (Queue)
        source2 - a queue (Queue)
    Returns:
        target - a queue (Queue)
    -------------------------------------------------------
    """

    target = Queue()

    while not source1.is_empty() and source2.is_empty:
        target.insert(source1.remove())
        target.append(source2.remove())
    while not source1.is_empty():
        target.append(source1.remove())
    while not source2.is_empty():
        target.append(source2.remove())
    return target


def pq_split_key(source, key):
    """
    -------------------------------------------------------
    Splits a priority queue into two depending on an external
    priority key. The source priority queue is empty when the method
    ends.
    Use: target1, target2 = pq_split_key(source, key)
    -------------------------------------------------------
    Parameters:
        source - a priority queue (Priority_Queue)
        key - a data object (?)
    Returns:
        target1 - a priority queue that contains all values
            with priority higher than key (Priority_Queue)
        target2 - priority queue that contains all values with
            priority lower than or equal to key (Priority_Queue)
    -------------------------------------------------------
    """
    target1 = Priority_Queue()
    target2 = Priority_Queue()

    while not source.is_empty():
        i = source.remove()
        if i > key:
            target1.insert(i)
        else:
            target2.insert(i)
    return target1, target2


def pq_triage(source, key):
    """
    -------------------------------------------------------
    Removes all values from source that have a priority
    less than key.
    Use: pq_triage(source, key)
    -------------------------------------------------------
    Parameters:
        source - a priority queue (Priority_Queue)
        key - a key value (?)
    Returns​‌‌‌​​​​‌:
        None
    -------------------------------------------------------
    """
    lst = []

    while not source.is_empty():
        i = source.remove()
        if i >= key:
            lst.append(i)
    for i in lst:
        source.insert(i)
    return


def purge(source, key):
    """
    -------------------------------------------------------
    Finds and removes all values in source that match key.
    Use: purge(source, key)
    -------------------------------------------------------
    Parameters:
        source - a List of values (List)
        key - a data element (?)
    Returns​‌‌‌​​​​‌:
        None
    -------------------------------------------------------
    """
    lst = []
    while not source.is_empty():
        i = source.remove_front()
        if i != key:
            lst.append(i)

    num = 0
    for v in lst:
        source.insert(num, v)
        num += 1
    return


def eval_expression(string):
    """
    -------------------------------------------------------
    Evaluates a postfix expression.
    Use: answer = postfix(string)
    -------------------------------------------------------
    Parameters:
        string - the postfix string to evaluate (str)
    Returns:
        answer - the result of evaluating string (float)
    -------------------------------------------------------
    """
    stack = Stack()

    token = string.split()

    for case in token:
        if case not in OPERATORS:
            stack.push(float(case))
        else:
            v1 = stack.pop()
            v2 = stack.pop()
            if case == "+":
                answer = v1 + v2
            elif case == "-":
                answer = v1 - v2
            elif case == "*":
                answer = v1 * v2
            elif case == "/":
                answer = v1 / v2
            stack.push(answer)
    answer = stack.pop()

    return answer


i = self._linear_search(key)
value = self._value.pop(i)
self._set_first()

i = self._linear_search(key)
value = deepcopy(self._values[i])
