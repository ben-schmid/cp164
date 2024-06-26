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
from functions import shift
# Constants

fv = open('pelee.txt')
fn = open('shift.txt', 'w')
n = 1
for line in fv:
    string = line
    estring = shift(string, n)
    fn.write(estring)

fv.close()
fn.close()
