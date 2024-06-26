"""
-------------------------------------------------------
Assignment 2, Task 5
-------------------------------------------------------
Author:  David Brown
ID:      999999999
Email:   dbrown@wlu.ca
__updated__ = "2023-02-02"
-------------------------------------------------------
"""
from Movie import Movie
from Movie_utilities import genre_counts, read_movies

fv = open('movies.txt', 'r')
movies = read_movies(fv)
fv.close()

counts = genre_counts(movies)
print("Genre             Count")
print("-----             -----")

for i in Movie.GENRE_CODES:
    print(f"{Movie.GENRES[i]:18s} {counts[i]:2d}")

print()
print("Done")
