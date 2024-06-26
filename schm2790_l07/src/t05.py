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

target = List()
source1 = List()
source2 = List()

list1 = [22, 33, 11, 55, 44]
list2 = [22, 33, 11, 55, 44]

for v in list1:
    source1.append(v)
# for v in list2:
#   source2.append(v)


print(target.intersection(source1, source2))
