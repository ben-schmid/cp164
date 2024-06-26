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

from Queue_linked import Queue

queue1 = Queue()
queue2 = Queue()

queue1.insert(11)
queue1.insert(22)
queue1.insert(33)
queue1.insert(44)

queue2.insert(11)
queue2.insert(22)
queue2.insert(33)
queue2.insert(44)

target1, target2 = queue1.split_alt()

for v in target1:
    print(v)
print()
for v in target2:
    print(v)
