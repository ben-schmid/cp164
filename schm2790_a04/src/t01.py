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
from Queue_circular import Queue
# Constants

queue = Queue()
queue.insert(4)
print("length", queue.__len__())
queue.insert(3)
print("Length", queue.__len__())
print("removed", queue.remove())
print("length", queue.__len__())
queue.insert(6)
print('length', queue.__len__())
queue.insert(7)
print('length', queue.__len__())
