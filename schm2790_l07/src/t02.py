"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Benjamin Schmid
ID:      169042790
Email:   schm2790@mylaurier.ca
__updated__ = "2023-03-09"
-------------------------------------------------------
"""
# Imports
from List_linked import List

lst_1 = List()


lst_2 = List()

list1 = [11, 22, 33]
list2 = [11, 22, 33]

for v in list1:
    lst_1.append(v)
for v in list2:
    lst_2.append(v)


print(lst_1.is_identical_r(lst_2))
