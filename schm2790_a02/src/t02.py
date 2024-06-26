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
from Movie_utilities import get_by_rating, read_movies
from Movie import Movie

fv = open("movies.txt", "r")
movies = read_movies(fv)


rating = float(input("Enter a rating: "))

while rating < Movie.MIN_RATING or rating > Movie.MAX_RATING:
    print("ERROR!")
    rating = float(input("Please enter a VALID rating between 0 and 10: "))

print("_" * 30)
print()

rmovies = get_by_rating(movies, rating)

for v in rmovies:
    print(v)
    print()


rmovies = get_by_rating(movies, rating)
