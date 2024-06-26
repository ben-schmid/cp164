"""
-------------------------------------------------------
Assignment 1, Task 3
-------------------------------------------------------
Author:  David Brown
ID:      999999999
Email:   dbrown@wlu.ca
__updated__ = "2023-01-29"
-------------------------------------------------------
"""
# Imports
from functions import find_subs

CASES = (
    ('a', 'a'),
    ('abc', 'b'),
    ('It was a really, really, big assignment.', 'real'),
)
for case in CASES:
    location = find_subs(case[0], case[1])
    print(f"find_subs('{case[0]}', '{case[1]}'): {location}")
print("Done")
