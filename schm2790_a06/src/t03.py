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
from Deque_linked import Deque

deque = Deque()

deque.insert_front(11)
deque.insert_rear(22)
deque.insert_front(33)
deque.insert_rear(44)
deque.insert_rear(55)
for v in deque:
    print(v)

deque._swap(deque._front, deque._front)
print()
for v in deque:
    print(v)

deque._swap(deque._front, deque._rear)
print()
for v in deque:
    print(v)

deque._swap(deque._front, deque._front._next)
print()
for v in deque:
    print(v)

deque._swap(deque._rear._prev, deque._rear)
print()
for v in deque:
    print(v)

deque._swap(deque._front._next, deque._rear._prev)
print()
for v in deque:
    print(v)

deque._swap(deque._front._next, deque._rear)
print()
for v in deque:
    print(v)

deque._swap(deque._rear._prev, deque._front)
print()
for v in deque:
    print(v)
