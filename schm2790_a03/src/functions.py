"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Benjamin Schmid
ID:      169042790
Email:   schm2790@mylaurier.ca
__updated__ = "2023-02-05"
-------------------------------------------------------
"""
# Imports
from Stack_array import Stack
from enum import Enum

# Constants
OPERATORS = "+-*/"
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

    i = 0
    while source.is_empty() == False:
        if i % 2 == 0:
            value = source.pop()
            target1.push(value)
        else:
            value = source.pop()
            target2.push(value)
        i += 1
    return target1, target2


def split_alt(self):
    """
    -------------------------------------------------------
    Splits the source stack into separate target stacks with values
    alternating into the targets. At finish source stack is empty.
    Use: target1, target2 = source.split_alt()
    -------------------------------------------------------
    Returns:
        target1 - contains alternating values from source (Stack)
        target2 - contains other alternating values from source (Stack)
    -------------------------------------------------------
    """
    target1 = Stack()
    target2 = Stack()

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
    chars = ""
    for c in string:
        if c.isalpha():
            chars += c.lower()

    length = len(chars)
    mid = 0
    if length == 0:
        palindrome = True
    else:
        mid = length // 2
        first = Stack()
        for i in range(mid):
            first.push(chars[i])
        if length % 2 == 0:
            second = chars[mid:]
        else:
            second = chars[mid + 1:]
        i = 0
        while palindrome and i < mid:
            second_half = second[i]
            first_half = first.pop()
            if second_half == first_half:
                i += 1
            else:
                palindrome = False
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
    chars = string.split()
    for i in chars:
        if i not in OPERATORS:
            stack.push(i)
        else:
            top = float(stack.pop())
            second = float(stack.pop())
            if i == "+":
                stack.push(second + top)
            elif i == "-":
                stack.push(second - top)
            elif i == "*":
                stack.push(second * top)
            else:
                stack.push(second / top)
    answer = stack.pop()
    return answer


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

    mirror = ''
    stack = Stack()
    i = 0

    if m in string:
        while i < len(string) and string[i] != m:
            chars = string[i]
            if chars not in valid_chars:
                mirror = MIRRORED.INVALID_CHAR
            else:
                stack.push(chars)
            i += 1

        left_length = i
        i += 1
        length_mid = left_length + 1
        right_length = len(string) - length_mid
        if right_length > left_length:
            mirror = MIRRORED.TOO_MANY_RIGHT
        elif right_length < left_length:
            mirror = MIRRORED.TOO_MANY_LEFT

        while i < len(string) and not stack.is_empty() and mirror == '':
            chars = string[i]
            letter = stack.pop()
            if chars not in valid_chars:
                mirror = MIRRORED.INVALID_CHAR
            else:
                if chars != letter:
                    mirror = MIRRORED.MISMATCHED
            i += 1

    else:
        mirror = MIRRORED.NOT_MIRRORED

    if mirror == '':
        mirror = MIRRORED.IS_MIRRORED
    return mirror


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
    location = "Start"
    dec = maze[location]
    path = []
    if "X" in dec:
        path.append("X")
    stack = Stack()
    while "X" not in dec:
        for i in dec:
            stack.push(i)
        location = stack.pop()
        if maze[location] != []:
            path.append(location)
        dec = maze[location]
        if "X" in dec:
            path.append("X")
    return path
