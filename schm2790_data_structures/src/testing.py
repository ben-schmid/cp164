"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Benjamin Schmid
ID:      169042790
Email:   schm2790@mylaurier.ca
__updated__ = "2023-01-16"
-------------------------------------------------------
"""
# Imports
from Movie import Movie
from Movie_utilities import read_genres
# Constants
movie = Movie('T1', 2000, 'D1', 5, [3, 4, 5, 8])
print(movie)

print()
print("-" * 40)
print()

s = Movie.genres_menu()
print(Movie.genres_menu())

print()
print("-" * 40)
print()

string = movie.genres_list_string()
print(string)

print()
print("-" * 40)
print()

genres = read_genres()
print(genres)
