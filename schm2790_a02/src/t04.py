"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Benjamin Schmid
ID:      169042790
Email:   schm2790@mylaurier.ca
__updated__ = "2023-01-29"
-------------------------------------------------------
"""
# Imports
from Movie_utilities import get_by_genres, read_movies

# Constants


fv = open("movies.txt", "r")
movies = read_movies(fv)

genres = [3, 4]
print(f"Genres: {genres}")
gmovies = get_by_genres(movies, genres)

for v in gmovies:
    print(v)
    print()
