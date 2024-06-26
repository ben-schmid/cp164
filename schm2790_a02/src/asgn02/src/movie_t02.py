"""
-------------------------------------------------------
Assignment 2, Task 2
-------------------------------------------------------
Author:  David Brown
ID:      999999999
Email:   dbrown@wlu.ca
__updated__ = "2023-02-02"
-------------------------------------------------------
"""
from Movie_utilities import get_by_rating, read_movies


fv = open("movies.txt", "r", encoding="utf-8")
movies = read_movies(fv)
fv.close()

rating = float(input("Enter rating (0 to quit): "))

while rating > 0:
    print()
    rmovies = get_by_rating(movies, rating)

    for movie in rmovies:
        print(movie)
        print()
    rating = float(input("Enter rating (0 to quit): "))
print()
print("Done")
