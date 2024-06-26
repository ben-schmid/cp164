"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Benjamin Schmid
ID:      169042790
Email:   schm2790@mylaurier.ca
__updated__ = "2023-01-18"
-------------------------------------------------------
"""
# Imports
from functions import file_analyze
# Constants

fv = open("file_stats.txt")

u, l, d, w, r = file_analyze(fv)

print(f"Upper Case Count: {u}")
print(f"Lower Case Count: {l}")
print(f"Digit Count: {d}")
print(f"White Space: {w}")
print(f"Random: {r}")

fv.close()
