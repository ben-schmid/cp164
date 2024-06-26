"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Benjamin Schmid
ID:      169042790
Email:   schm2790@mylaurier.ca
__updated__ = "2023-03-03"
-------------------------------------------------------
"""
# Imports
from functions import stack_split_alt
from Stack_array import Stack
# Constants
source = Stack()


s1 = [5, 4, 3, 2, 1]

for i in s1:
    source.push(i)
for v in source:
    print(v)
print()

target1, target2 = stack_split_alt(source)

for v in target1:
    print(v)
print()
for k in target2:
    print(k)
