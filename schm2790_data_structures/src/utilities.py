"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Benjamin Schmid
ID:      169042790
Email:   schm2790@mylaurier.ca
__updated__ = "2023-02-10"
-------------------------------------------------------
"""
# Imports
from Stack_array import Stack
from Movie import Movie
from Queue_array import Queue
from Priority_Queue_array import Priority_Queue
from List_array import List
from copy import deepcopy
# Constants


def array_to_stack(stack, source):
    """
    -------------------------------------------------------
    Pushes contents of source onto stack. At finish, source is empty.
    Last value in source is at bottom of stack,
    first value in source is on top of stack.
    Use: array_to_stack(stack, source)
    -------------------------------------------------------
    Parameters:
        stack - a Stack object (Stack)
        source - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    n = len(source)

    i = 0
    while i < n:
        stack.push(source[n - 1 - i])
        source.pop(n - 1 - i)
        i += 1
    return


def stack_to_array(stack, target):
    """
    -------------------------------------------------------
    Pops contents of stack into target. At finish, stack is empty.
    Top value of stack is at end of target,
    bottom value of stack is at beginning of target.
    Use: stack_to_array(stack, target)
    -------------------------------------------------------
    Parameters:
        stack - a Stack object (Stack)
        target - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    while not stack.is_empty():
        target.insert(0, stack.pop())
    return


def stack_test(source):
    """
    -------------------------------------------------------
    Tests the methods of Stack for empty and
    non-empty stacks using the data in source:
    is_empty, push, pop, peek
    (Testing pop and peek while empty throws exceptions)
    Use: stack_test(source)
    -------------------------------------------------------
    Parameters:
        source - list of data (list of ?)
    Returns:
        None
    -------------------------------------------------------
    """
    stack = Stack()

    if stack.is_empty():
        print("The stack is empty")
        for j in source:
            stack.push(j)
            print(f'{j} was pushed to the stack')
    else:
        print("The stack isn't empty")
        for j in source:
            stack.push(j)
            print(f"{j} has been pushed to the stack")

    if stack.is_empty():
        print("The stack is still empty")
    else:
        print("The stack isn't empty")

    print("The top of the stack: {}".format(stack.peek()))
    print("The last item removed from the stack: {}".format(stack.pop()))
    return


def array_to_queue(queue, source):
    """
    -------------------------------------------------------
    Inserts contents of source into queue. At finish, source is empty.
    Last value in source is at rear of queue,
    first value in source is at front of queue.
    Use: array_to_queue(queue, source)
    -------------------------------------------------------
    Parameters:
        queue - a Queue object (Queue)
        source - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    n = len(source)

    i = 0
    while i < n:
        queue.insert(source[0])
        source.pop(0)
        i += 1
    return


def queue_to_array(queue, target):
    """
    -------------------------------------------------------
    Removes contents of queue into target. At finish, queue is empty.
    Front value of queue is at front of target,
    rear value of queue is at end of target.
    Use: queue_to_array(queue, target)
    -------------------------------------------------------
    Parameters:
        queue - a Queue object (Queue)
        target - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    n = len(queue)
    i = 0
    while i < n:
        target.append(queue.remove())
        i += 1
    return


def queue_test(a):
    """
    -------------------------------------------------------
    Tests queue implementation.
  Tests the methods of Queue are tested for both empty and
  non-empty queues using the data in a:
        is_empty, insert, remove, peek, len
    Use: queue_test(a)
    -------------------------------------------------------
    Parameters:
        a - list of data (list of ?)
    Returns:
        None
    -------------------------------------------------------
    """
    q = Queue()
    if q.is_empty():
        print('Queue empty')
    else:
        print("Queue is not empty")
    for i in a:
        q.insert(i)
    print("First item in queue is {}".format(q.peek()))
    print("The last item removed is {}".format(q.remove()))
    print("First item in queue is now {}".format(q.peek()))

    # tests for the queue methods go here
    # print the results of the method calls and verify by hand

    return


def array_to_pq(pq, source):
    """
    -------------------------------------------------------
    Inserts contents of source into pq. At finish, source is empty.
    Last value in source is at rear of pq,
    first value in source is at front of pq.
    Use: array_to_pq(pq, source)
    -------------------------------------------------------
    Parameters:
        pq - a Priority_Queue object (Priority_Queue)
        source - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    n = len(source)

    i = 0
    while i < n:
        pq.insert(source[0])
        source.pop(0)
        i += 1
    return


def pq_to_array(pq, target):
    """
    -------------------------------------------------------
    Removes contents of pq into target. At finish, pq is empty.
    Highest priority value in pq is at front of target,
    lowest priority value in pq is at end of target.
    Use: pq_to_array(pq, target)
    -------------------------------------------------------
    Parameters:
        pq - a Priority_Queue object (Priority_Queue)
        target - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    n = len(pq)
    i = 0
    while i < n:
        target.append(pq.remove())
        i += 1
    return


def priority_queue_test(a):
    """
    -------------------------------------------------------
    Tests priority queue implementation.
    Test the methods of Priority_Queue are tested for both empty and
    non-empty priority queues using the data in a:
        is_empty, insert, remove, peek
    Use: priority_queue_test(a)
    -------------------------------------------------------
    Parameters:
        a - list of data (list of ?)
    Returns:
        None
    -------------------------------------------------------
    """
    pq = Priority_Queue()

    if pq.is_empty():
        print('Queue empty')
    else:
        print("Queue is not empty")
    for i in a:
        pq.insert(i)
    print("First item in queue is {}".format(pq.peek()))
    print("The last item removed is {}".format(pq.remove()))
    print("First item in queue is now {}".format(pq.peek()))

    # tests for the priority queue methods go here
    # print the results of the method calls and verify by hand

    return


def array_to_list(llist, source):
    """
    -------------------------------------------------------
    Appends contests of source to llist. At finish, source is empty.
    Last element in source is at rear of llist,
    first element in source is at front of llist.
    Use: array_to_list(llist, source)
    -------------------------------------------------------
    Parameters:
        llist - a List object (List)
        source - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    while len(source) > 0:
        llist.append(source.pop(0))
    return


def list_to_array(llist, target):
    """
    -------------------------------------------------------
    Removes contents of llist into target. At finish, llist is empty.
    Front element of llist is at front of target,
    rear element of llist is at rear of target.
    Use: list_to_array(llist, target)
    -------------------------------------------------------
    Parameters:
        llist - a List object (List)
        target - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    while len(llist) > 0:
        target.append(llist.pop(0))
    return


def list_test(source):
    """
    -------------------------------------------------------
    Tests List implementation.
    The methods of List are tested for both empty and
    non-empty lists using the data in source
    Use: list_test(source)
    -------------------------------------------------------
    Parameters:
        source - list of data (list of ?)
    Returns:
        None
    -------------------------------------------------------
    """
    lst = List()

    if lst.is_empty:
        print('empty list')
    for i in source:
        lst.append(deepcopy(i))
        print('item added to list')

    for j in source:
        if len(lst) > 9:
            lst.insert(10, deepcopy(j))
            print(j, "was added to list")
    if not lst.is_empty():
        print('list is not empty')
    print("first is list {}".format(lst.peek()))
    print("largest {}".format(lst.max()))
    print("item removed {}".format(lst.remove(lst.min())))
    print("The smallest item in the list is {}\ and it's index is {}.\nIt is in the list {} time(s).".format(
        lst.find(lst.min()), lst.index(lst.min()), lst.count(lst.min())))
    print()
