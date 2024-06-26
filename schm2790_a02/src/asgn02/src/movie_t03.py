"""
-------------------------------------------------------
Assignment 2, Task 3
-------------------------------------------------------
Author:  David Brown
ID:      999999999
Email:   dbrown@wlu.ca
__updated__ = "2023-02-02"
-------------------------------------------------------
"""
from Movie import Movie
from Movie_utilities import get_by_genre, read_movies


fv = open("movies.txt", "r", encoding="utf-8")
movies = read_movies(fv)
fv.close()

print(Movie.genres_menu())
genre = int(input("Enter a genre (-1 to quit): "))

while genre > -1:
    print()
    gmovies = get_by_genre(movies, genre)

    for movie in gmovies:
        print(movie)
        print()
    print(Movie.genres_menu())
    genre = int(input("Enter a genre (-1 to quit): "))

print()
print("Done")
