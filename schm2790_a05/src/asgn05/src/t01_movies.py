"""
-------------------------------------------------------
Tests array-based list
-------------------------------------------------------
Author:  David Brown
ID:      999999999
Email:   dbrown@wlu.ca
__updated__ = "2022-02-12"
-------------------------------------------------------
"""
# Imports
from List_array import List
from Movie_utilities import read_movies

# Constants
SEP = "-" * 60


def list_test(a):
    l1 = List()
    l2 = List()
    l3 = List()
    # Grab an arbitrary value as a key value
    key = a[0]

    print("Empty list: ")
    print(f"  Size: {len(l1)}")
    print(f"  Empty: {l1.is_empty()}")
    print(f"  Key: {key}")
    print(f"  Key in list: {key in l1}")

    print(SEP)
    print('Fill the list.')

    for v in a:
        l1.insert(0, v)

    print(SEP)

    for v in l1:
        print(v)
    print()

    print(f"  Max: {l1.max()}")
    print()
    print(f"  Min: {l1.min()}")
    print()
    print('Using Key Value')
    print(f"  Key: {key}")
    print()
    print(f"  Key in list: {key in l1}")
    print()
    print(f"  Key count {l1.count(key)} times")
    print()
    print(f"  Find value: {l1.find(key)}")
    print()
    print("Removing a node:")
    print(l1.remove(key))

    print(SEP)
    print("Adding data again:")

    for v in a:
        l1.insert(0, v)
    print(SEP)
    print(f"Length of l1: {len(l1)}")
    print("Remove Many:")
    key = a[1]
    l1.remove_many(key)
    print(f"Length of l1: {len(l1)}")

    print(SEP)
    print(f"Length of l1: {len(l1)}")
    print("Clean:")
    l1.clean()
    print(f"Length of l1: {len(l1)}")

    print(SEP)
    print("Intersection with empty list:")
    l3.intersection(l1, l2)
    print(f"Length of l1: {len(l1)}")
    print(f"Length of l2: {len(l2)}")
    print(f"Length of l3: {len(l3)}")

    for v in a:
        l2.insert(0, v)

    print(SEP)
    print("Intersection with full list:")
    l3 = List()
    l3.intersection(l1, l2)
    print(f"Length of l1: {len(l1)}")
    print(f"Length of l2: {len(l2)}")
    print(f"Length of l3: {len(l3)}")

    print(SEP)
    print("Union with empty list:")
    l2 = List()
    l3 = List()
    l3.union(l1, l2)
    print(f"Length of l1: {len(l1)}")
    print(f"Length of l2: {len(l2)}")
    print(f"Length of l3: {len(l3)}")

    print(SEP)
    print("Union with full list:")

    for v in a:
        l2.insert(0, v)

    l3 = List()
    l3.union(l1, l2)
    print(f"Length of l1: {len(l1)}")
    print(f"Length of l2: {len(l2)}")
    print(f"Length of l3: {len(l3)}")

    return


filename = "movies.txt"
fv = open(filename, "r", encoding="utf-8")
movies = read_movies(fv)
fv.close()
list_test(movies)
