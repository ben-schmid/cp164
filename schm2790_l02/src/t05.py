"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Benjamin Schmid
ID:      169042790
Email:   schm2790@mylaurier.ca
__updated__ = "2023-01-27"
-------------------------------------------------------
"""
# Imports
from utilities import stack_test
from Movie_utilities import read_movies

fv = open("movies.txt", 'r')
source = read_movies(fv)

stack_test(source)
