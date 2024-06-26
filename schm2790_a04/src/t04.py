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
from Queue_array import Queue

source1 = Queue()
source2 = Queue()

s1 = [1, 2, 3, 4]
for i in s1:
    source1.insert(i)
s2 = [5, 6, 7, 8]
for j in s2:
    source2.insert(j)

target = Queue()
target.combine(source1, source2)


target_list = []
for i in target:
    target_list.append(i)

print(target_list)
