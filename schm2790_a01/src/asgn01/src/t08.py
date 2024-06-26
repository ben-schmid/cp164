"""
-------------------------------------------------------
Assignment 1, Task 8
-------------------------------------------------------
Author:  David Brown
ID:      999999999
Email:   dbrown@wlu.ca
__updated__ = "2023-01-27"
-------------------------------------------------------
"""
# Imports
from functions import pig_latin

CASES = (
    "car",
    "yard",
    "lynx",
    "art",
    "David",
    "track"
)
for case in CASES:
    results = pig_latin(case)
    print(f"pig_latin('{case}'): {results}")
print("Done")
