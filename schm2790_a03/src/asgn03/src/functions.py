"""
-------------------------------------------------------
Assignment 3 Functions
-------------------------------------------------------
Author:  David Brown
ID:      999999999
Email:   dbrown@wlu.ca
__updated__ = "2023-02-07"
-------------------------------------------------------
"""
# imports
from enum import Enum

from Stack_array import Stack


# Constants
LEFT = '([{<'
RIGHT = ')]}>'
PAIRS = ('()', '[]', '{}', '<>')

# Dictionary constants
OPERATORS = {'**': 3, '*': 2, '//': 2, '/': 2, '+': 1, '-': 1}

# Enumerated constants
MIRRORED = Enum('MIRRORED',
                {'IS_MIRRORED': "is a mirror", 'TOO_MANY_LEFT': "too many characters in L",
                 'TOO_MANY_RIGHT': "too many characters in R", 'MISMATCHED': "L and R don't match",
                 'INVALID_CHAR': "invalid character", 'NOT_MIRRORED': "no mirror character"})


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
        # toggle the left/right value
        left = not left
    return target1, target2


def is_palindrome_stack(string):
    """
    -------------------------------------------------------
    Determines if string is a palindrome. Ignores case, spaces, digits and
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
    # Clean up the string
    temp = ""

    for c in string:
        if c.isalpha():
            temp = temp + c.lower()

    n = len(temp)
    # Get the midpoint of the cleaned up string
    mid = n // 2
    i = 0
    s = Stack()

    while i < mid:
        # Copy the first half of the string onto the stack.
        s.push(temp[i])
        i += 1

    if n % 2 == 0:
        # String is even in length - move to next character
        i = mid
    else:
        # String is odd in length - skip over middle character
        i = mid + 1

    while palindrome and i < n:
        # Walk through the last half of the string, comparing it to the stack
        # contents
        if temp[i] != s.pop():
            palindrome = False
        else:
            i += 1
    return palindrome


def postfix(string):
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
    # Tokenize the string
    tokens = string.split()
    answer = 0.0

    for case in tokens:
        if case not in OPERATORS.keys():
            stack.push(float(case))
        else:
            v1 = stack.pop()
            v2 = stack.pop()

            if case == '+':
                answer = v2 + v1
            elif case == '*':
                answer = v2 * v1
            elif case == '-':
                answer = v2 - v1
            elif case == '/':
                answer = v2 / v1
            stack.push(answer)
    # The final result is the last element on the stack
    answer = stack.pop()
    return answer


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


def is_mirror_stack(string, valid_chars, m):
    """
    -------------------------------------------------------
    Determines if string is a mirror of characters in valid_chars around the pivot m.
    A mirror is of the form LmR, where L is the reverse of R, and L and R
    contain only characters in valid_chars.
    Use: mirror = is_mirror_stack(string, valid_chars, m)
    -------------------------------------------------------
    Parameters:
        string - a string (str)
        valid_chars - a string of valid characters (str)
        m - the mirror pivot string (str - one character not in valid_chars)
    Returns:
        mirror - the state of the string (Enum MIRRORED)
    -------------------------------------------------------
    """
    assert m not in valid_chars, \
        f"cannot use '{m}' as the mirror character"

    s = Stack()
    mirror = MIRRORED.IS_MIRRORED
    n = len(string)
    i = 0

    # read L
    while mirror == MIRRORED.IS_MIRRORED and i < n and string[i] != m:

        if string[i] not in valid_chars:
            mirror = MIRRORED.INVALID_CHAR
        else:
            s.push(string[i])
            i += 1

    if i >= n:
        mirror = MIRRORED.NOT_MIRRORED
    else:
        # skip over m
        i += 1

    while mirror == MIRRORED.IS_MIRRORED and i < n and not s.is_empty():
        c = s.pop()

        if string[i] != c:
            mirror = MIRRORED.MISMATCHED
        else:
            i += 1

    if mirror == MIRRORED.IS_MIRRORED:
        if i < n:
            # characters in R left over
            mirror = MIRRORED.TOO_MANY_RIGHT
        elif not s.is_empty():
            # not enough characters in R
            mirror = MIRRORED.TOO_MANY_LEFT

    return mirror
