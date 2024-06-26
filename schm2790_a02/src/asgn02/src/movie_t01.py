"""
-------------------------------------------------------
Assignment 2, Task 1
-------------------------------------------------------
Author:  David Brown
ID:      999999999
Email:   dbrown@wlu.ca
__updated__ = "2023-02-02"
-------------------------------------------------------
"""
from Movie_utilities import get_by_year, read_movies


fv = open("movies.txt", "r", encoding="utf-8")
movies = read_movies(fv)
fv.close()

year = int(input("Enter year (0 to quit): "))

while year > 0:
    print()
    ymovies = get_by_year(movies, year)

    for movie in ymovies:
        print(movie)
        print()
        # or
        # print(movie.title)
    year = int(input("Enter year (0 to quit): "))

print()
print("Done")
