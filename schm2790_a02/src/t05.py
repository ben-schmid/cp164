"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Benjamin Schmid
ID:      169042790
Email:   schm2790@mylaurier.ca
__updated__ = "2023-02-02"
-------------------------------------------------------
"""
# Imports
from Movie_utilities import genre_counts, read_movies
# Constants

fv = open("movies.txt", "r")
movies = read_movies(fv)
counts = genre_counts(movies)
print(counts)
