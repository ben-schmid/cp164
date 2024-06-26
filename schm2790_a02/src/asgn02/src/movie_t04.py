"""
-------------------------------------------------------
Assignment 2, Task 4
-------------------------------------------------------
Author:  David Brown
ID:      999999999
Email:   dbrown@wlu.ca
__updated__ = "2023-02-02"
-------------------------------------------------------
"""
from Movie_utilities import get_by_genres, read_movies, read_genres


fv = open("movies.txt", "r", encoding="utf-8")
movies = read_movies(fv)
fv.close()

cont = 'Y'

while cont.upper() == 'Y':
    genres = read_genres()
    print()
    gmovies = get_by_genres(movies, genres)

    for movie in gmovies:
        print(movie)
        print()
    cont = input("Continue (Y/N): ")
print()
print("Done")
