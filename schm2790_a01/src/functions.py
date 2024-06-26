"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Benjamin Schmid
ID:      169042790
Email:   schm2790@mylaurier.ca
__updated__ = "2023-01-20"
-------------------------------------------------------
"""
# Imports

# Constants
VOWELS = 'A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u'
VOWELS_Y = 'A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u', 'Y', 'y'
ALPHABET = 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',\
    'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f',\
    'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'


def clean_list(values):
    """
    -------------------------------------------------------
    Removes all duplicate values from a list: values contains
    only one copy of each of its integers. The order of values
    must be preserved.
    Use: clean_list(values)
    -------------------------------------------------------
    Parameters:
        values - a list of integers (list of int)
    Returns:
        None
    -------------------------------------------------------
    """
    list = []
    i = 0

    while i < len(values):
        if (values[i] in list) == True:
            values.pop(i)
        else:
            list.append(values[i])
            i += 1

    return


def file_analyze(fv):
    """
    -------------------------------------------------------
    Analyzes the characters in a file.
    The contents of the file must be unchanged.
    Use: u, l, d, w, r = file_analyze(fv)
    -------------------------------------------------------
    Parameters:
        fv - an already open file reference (file variable)
    Returns:
        u - the number of uppercase letters in the file (int)
        l - the number of lowercase letters in the file (int)
        d - the number of digits in the file (int)
        w - the number of whitespace characters in the file (int)
        r - the number of remaining characters in the file (int)
    -------------------------------------------------------
    """

    u = 0
    l = 0
    d = 0
    w = 0
    r = 0

    for line in fv:
        for i in line:
            if i.isupper() is True:
                u += 1
            elif i.islower() is True:
                l += 1
            elif i.isdigit() is True:
                d += 1
            elif i.isspace() is True:
                w += 1
            else:
                r += 1
    return u, l, d, w, r


def find_subs(string, sub):
    """
    -------------------------------------------------------
    Finds the indices of the locations of sub within string,
        left to right.
    Use: locations = find_subs(string, sub)
    -------------------------------------------------------
    Parameters:
        string - a string to evaluate (str)
        sub - a substring to locate in string (str)
    Returns:
        locations - an ordered list of the indices of the locations
            of sub within string (list of int)
    -------------------------------------------------------
    """

    locations = []
    count = 0
    while string.find(sub) > -1:
        locations.append(string.find(sub) + count)
        count += string.find(sub) + len(sub)
        string = string[string.find(sub) + len(sub):len(string)]
    return locations


def is_leap_year(year):
    """
    -------------------------------------------------------
    Leap year determination.
    Use: leap_year = is_leap_year(year)
    -------------------------------------------------------
    Parameters:
        year - year to determine if it is a leap year (int > 0)
    Returns:
        leap_year - True if year is a leap year, False otherwise (boolean)
    -------------------------------------------------------
    """

    leap_year = False

    if year % 4 == 0 and year % 100 != 0:
        leap_year = True
    elif year % 100 == 0 and year % 400 == 0:
        leap_year = True

    return leap_year


def is_valid(name):
    """
    -------------------------------------------------------
    Determines if name is a valid Python variable name.
    Variables names must start with a letter or an underscore.
    The rest of the variable name may consist of letters, numbers
    and underscores.
    Use: valid = is_valid(name)
    -------------------------------------------------------
    Parameters:
        name - a string to test as a Python variable name (str)
    Returns:
        valid - True if name is a valid Python variable name,
            False otherwise (boolean)
    -------------------------------------------------------
    """

    valid = True
    if name.find("_") > -1:
        name = name.replace("_", "")
    if name.isalnum():
        valid = True
        if name[:1].isdigit():
            valid = False
    else:
        valid = False
    if name.isspace():
        valid = False
    return valid


def matrix_transpose(a):
    """
    -------------------------------------------------------
    Transpose the contents of matrix a.
    Use: b = matrix_transpose(a):
    -------------------------------------------------------
    Parameters:
        a - a 2D list (list of lists of ?)
    Returns:
        b - the transposed matrix (list of lists of ?)
    -------------------------------------------------------
    """
    b = []
    i = 0
    j = 0

    while i < len(a[0]):
        b.append([])
        j = 0
        while j < len(a):
            b[i].append(a[j][i])
            j += 1
        i += 1

    return b


def matrixes_multiply(a, b):
    """
    -------------------------------------------------------
    Multiplies the contents of matrixes a and b.
    If a is mxn in size, and b is nxp in size, then c is mxp.
    a and b must be unchanged.
    Use: c = matrixes_multiply(a, b)
    -------------------------------------------------------
    Parameters:
        a - a 2D list (2D list of int/float)
        b - a 2D list (2D list of int/float)
    Returns:
        c - the matrix multiple of a and b (2D list of int/float)
    -------------------------------------------------------
    """

    c = []
    a_row = len(a)
    a_col = len(a[0])
    b_row = len(b)
    b_col = len(b[0])

    if a_col == b_row:
        for i in range(a_row):
            c.append([])
            for j in range(b_col):
                result = 0
                for r in range(b_row):
                    result += a[i][r] * b[r][j]
                c[i].append(result)
    return c


def pig_latin(word):
    """
    -------------------------------------------------------
    Converts a word to Pig Latin. The conversion is:
    - if a word begins with a vowel, add "way" to the end of the word.
    - if the word begins with consonants, move the leading consonants to
    the end of the word and add "ay" to the end of that.
    "y" is treated as a consonant if it is the first character in the word,
    and as a vowel for anywhere else in the word.
    Preserve the case of the word - i.e. if the first character of word
    is upper-case, then the new first character should also be upper case.
    Use: pl = pig_latin(word)
    -------------------------------------------------------
    Parameters:
        word - a string to convert to Pig Latin (str)
    Returns:
        pl - the Pig Latin version of word (str)
    ------------------------------------------------------
    """

    i = 0
    pl = word
    if word.startswith(VOWELS_Y):
        pl = word + "way"
    else:
        while pl[i] not in VOWELS:
            pl = pl[1:] + pl[:1]
        pl += "ay"
    pl = pl.lower()
    if word[:1].isupper():
        pl = pl.capitalize()

    return pl


def shift(string, n):
    """
    -------------------------------------------------------
    Encipher a string using a shift cipher.
    Only letters are enciphered, and the returned string is
    in upper case.
    Use: estring = shift(string, n):
    -------------------------------------------------------
    Parameters:
        string - string to encipher (str)
        n - the number of letters to shift (int)
    Returns:
        estring - the enciphered string (str)
    -------------------------------------------------------
    """

    estring = ''

    i = 0

    while i < len(string):
        j = 0
        while string[i] != ALPHABET[j]:
            j += 1
        calc = n + j
        estring += ALPHABET[calc]
        i += 1
    return estring
