"""
-------------------------------------------------------
[Movie_utilities testing]
-------------------------------------------------------
Author:  Benjamin Schmid
ID:      169042790
Email:   schm2790@mylaurier.ca
__updated__ = "2023-01-19"
-------------------------------------------------------
"""
# Imports
from Movie_utilities import get_movie, read_movie, read_movies


fv = open("movies.txt", "r")
movies = read_movies(fv)

for i in movies:
    print(i)

movie = get_movie()
print(movie)

fv.close()
