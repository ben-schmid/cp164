"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Benjamin Schmid
ID:      169042790
Email:   schm2790@mylaurier.ca
__updated__ = "2023-02-04"
-------------------------------------------------------
"""
# Imports
from functions import stack_split_alt

from functions import stack_split_alt
from Stack_array import Stack

array = [5, 7, 8, 9, 12, 14, 8]
print('Source {}'.format(array))
print()

source = Stack()

for s in array:
    source.push(s)

target1, target2 = stack_split_alt(source)
while target1.is_empty() == False:
    print('target1 {}'.format(target1.pop()))
print()
while target2.is_empty() == False:
    print('target2 {}'.format(target2.pop()))
