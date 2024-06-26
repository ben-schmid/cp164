"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Benjamin Schmid
ID:      169042790
Email:   schm2790@mylaurier.ca
__updated__ = "2023-03-12"
-------------------------------------------------------
"""
# Imports
from Priority_Queue_linked import Priority_Queue

queue1 = Priority_Queue()
queue2 = Priority_Queue()

queue1.insert(11)
queue1.insert(22)
queue1.insert(33)
queue1.insert(44)

queue2.insert(11)
queue2.insert(22)
queue2.insert(33)
queue2.insert(44)

target = Priority_Queue()

target.combine(queue1, queue2)
for v in target:
    print(v)
