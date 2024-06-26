"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Benjamin Schmid
ID:      169042790
Email:   schm2790@mylaurier.ca
__updated__ = "2023-02-11"
-------------------------------------------------------
"""
# Imports
from Priority_Queue_array import Priority_Queue
# Constants

source = Priority_Queue()
s1 = [1, 2, 3, 4, 5, 6, 7, 8]
for i in s1:
    source.insert(i)

key = 5

target1, target2 = source.split_key(key)

while target1.is_empty() is False:
    print('target1: {}'.format(target1.remove()))
while target2.is_empty() is False:
    print('target2: {}'.format(target2.remove()))
print('key:', key)
