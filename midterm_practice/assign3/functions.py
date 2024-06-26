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
from Stack_array import Stack

# Constants


def stack_split_alt(source):
    """
    -------------------------------------------------------
    Splits the source stack into separate target stacks.
    When finished source stack is empty. Values are
    pushed alternately onto the returned target stacks.
    Use: target1, target2 = stack_split_alt(source)
    -------------------------------------------------------
    Parameters:
        source - the stack to split into two parts (Stack)
    Returns:
        target1 - contains alternating values from source (Stack)
        target2 - contains other alternating values from source (Stack)
    -------------------------------------------------------
    """
    target1 = Stack()
    target2 = Stack()

    left = True

    while not source.is_empty():
        if left:
            target1.push(source.pop())
        else:
            target2.push(source.pop())
        left = not left
    return target1, target2


def is_palindrome_stack(string):
    """
    -------------------------------------------------------
    Determines if string is a palindrome. Ignores case, digits, spaces, and
    punctuation in string.
    Use: palindrome = is_palindrome_stack(string)
    -------------------------------------------------------
    Parameters:
        string - a string (str)
    Returns:
        palindrome - True if string is a palindrome, False otherwise (bool)
    -------------------------------------------------------
    """
    palindrome = True

    clean = ""
    for c in string:
        if c.isalpha():
            clean = clean + c.lower()

    length = len(clean)

    mid = length // 2

    s = Stack()
    i = 0

    while i < mid:
        s.push(clean[i])
        i += 1

    if mid % 2 == 0:
        i = mid
    else:
        i = mid + 1
    while palindrome and i < length:
        if clean[i] != s.pop():
            palindrome = False
        else:
            i += 1
    return palindrome


def stack_maze(maze):
    """
    -------------------------------------------------------
    Solves a maze using Depth-First search.
    Use: path = stack_maze(maze)
    -------------------------------------------------------
    Parameters:
        maze - dictionary of points in a maze, where each point
            represents a corridor end or a branch. Dictionary
            keys are the name of the point followed by a list of
            branches, if any. First point is named 'Start', exit
            is named 'X' (dict)
    Returns:
        path - list of points visited before the exit is reached,
            None if there is no exit (list of str)
    -------------------------------------------------------
    """
    stack = Stack()
    path = []
    # Define starting point
    point = 'Start'

    while point != 'X' and path is not None:
        points = maze[point]

        for point in points:
            if point not in path:
                # Push only points not already visited
                stack.push(point)

        if stack.is_empty():
            # Nowhere left to go
            path = None
        else:
            # Get the next point to visit
            point = stack.pop()
            path.append(point)
    return path
