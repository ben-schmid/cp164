"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Benjamin Schmid
ID:      169042790
Email:   schm2790@mylaurier.ca
__updated__ = "2023-04-16"
-------------------------------------------------------
"""
# Imports
from functions import hash_table
from Movie_utilities import read_movies


fv = open('movies.txt', 'r')

a = read_movies(fv)
hash_table(30, a)

fv.close()
