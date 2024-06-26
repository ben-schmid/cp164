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

# Constants

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
