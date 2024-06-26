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
# Import
from Movie_utilities import get_by_year, read_movies
# Constants

fv = open("movies.txt", "r")
movies = read_movies(fv)

year = int(input("Enter the year "))
print("_" * 30)
print()

ymovies = get_by_year(movies, year)

for v in ymovies:
    print(v)
    print()
