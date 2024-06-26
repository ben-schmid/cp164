"""
-------------------------------------------------------
Assignment 3, Task 6
-------------------------------------------------------
Author:  David Brown
ID:      999999999
Email:   dbrown@wlu.ca
__updated__ = "2023-02-07"
-------------------------------------------------------
"""
# Imports
from functions import is_mirror_stack

print("Testing 'is_mirror_stack'")
print()
CASES = (
    ('ama', 'a', 'm'), ('a', 'a', 'm'), ('ama', 'g', 'm'),
    ('aama', 'a', 'm'), ('amaa', 'a', 'm'), ('amb', 'ab', 'm'),
    ("cmc", "ab", "m"), ("zzxzxzxzz", "xyz", "u"),
    ("zzxzuzx", "xyz", "u"),
)

for case in CASES:
    mirror = is_mirror_stack(case[0], case[1], case[2])
    print(
        f"is_mirror_stack({case[0]}, {case[1]}, {case[2]}) -> {mirror}: {mirror.value}")
print("Done")
