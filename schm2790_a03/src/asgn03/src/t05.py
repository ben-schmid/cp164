"""
-------------------------------------------------------
Assignment 3, Task 5
-------------------------------------------------------
Author:  David Brown
ID:      999999999
Email:   dbrown@wlu.ca
__updated__ = "2023-02-07"
-------------------------------------------------------
"""
# Imports
from functions import stack_maze


CASES = (
    {'Start': ['X']},
    {'Start': ['A'], 'A': ['B', 'C'], 'B': [], 'C': ['D', 'E'],
        'D': [], 'E': ['F', 'X'], 'F': ['G', 'H'], 'G': [], 'H': []},
    {'Start': ['A'], 'A': []},
    {'Start': ['A', 'B'], 'A': [], 'B': ['C'], 'C': ['D'], 'D': ['X', 'B']}
)
print("Testing 'stack_maze'")
print()

for maze in CASES:
    path = stack_maze(maze)
    print(f"stack_maze({maze}) -> {path}")
print("Done")
