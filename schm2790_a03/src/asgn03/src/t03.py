"""
-------------------------------------------------------
Assignment 3, Task 3
-------------------------------------------------------
Author:  David Brown
ID:      999999999
Email:   dbrown@wlu.ca
__updated__ = "2023-02-07"
-------------------------------------------------------
"""
# Imports
from functions import is_palindrome_stack

CASES = ("", "a", "aa", "aaa", "otto", "RaceCar", "Able was I ere I saw Elba",
         "A man, a plan, a canal, Panama!", "David")
print("Testing 'is_palindrome_stack'")
print()

for string in CASES:
    palindrome = is_palindrome_stack(string)
    print(f"is_palindrome_stack('{string}') -> {palindrome}")
print("Done")
