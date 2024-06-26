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
from functions import queue_combine
from Queue_array import Queue
# Constants

source1 = Queue()
source2 = Queue()
s1 = [1, 2, 3, 4]
s2 = [5, 6, 7, 8]
for i in s1:
    source1.insert(i)
for j in s2:
    source2.insert(j)
target = queue_combine(source1, source2)
lst = []
for t in target:
    lst.append(t)
print(lst)
