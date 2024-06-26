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
from functions import clean_list
# Constants
values = [1, 2, 0, 1, 4, 1, 1, 2, 2, 5, 4,
          3, 1, 3, 3, 4, 2, 4, 3, 1, 3, 0, 3, 0, 0]

print(f'Values: {values}')
clean_list(values)

print(f'Cleaned: {values}')
