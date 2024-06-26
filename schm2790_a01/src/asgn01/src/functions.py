"""
-------------------------------------------------------
CP164: Assignment 1
-------------------------------------------------------
Author:  David Brown
ID:      999999999
Email:   dbrown@wlu.ca
__updated__ = "2023-01-29"
-------------------------------------------------------
"""
# Constants
VOWELS = 'aeiouAEIOU'
ALPHA = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
ALPHA_SIZE = len(ALPHA)
CIPHERTEXT = 'AVIBROWNZCEFGHJKLMPQSTUXYD'


def clean_list(values):
    """
    -------------------------------------------------------
    Removes all duplicate values from a list: values contains
    only one copy of each of its integers
    Use: clean_list(values)
    -------------------------------------------------------
    Parameters:
        values - a list of integers (list of int)
    Returns:
        None
    -------------------------------------------------------
    """
    i = 0

    while i < len(values):
        j = i + 1

        while j < len(values):
            if values[j] == values[i]:
                values.pop(j)
            else:
                j += 1
        i += 1
    return


def file_analyze(fv):
    """
    -------------------------------------------------------
    Analyzes the characters in a file.
    The contents of the file must be unchanged.
    Use: upp, low, dig, whi, rem = file_analyze(fv)
    -------------------------------------------------------
    Parameters:
        fv - an already open file reference (file variable)
    Returns:
        upp - the number of uppercase letters in the file (int)
        low - the number of lowercase letters in the file (int)
        dig - the number of digits in the file (int)
        whi - the number of whitespace characters in the file (int)
        rem - the number of remaining characters in the file (int)
    -------------------------------------------------------
    """
    upp = 0
    low = 0
    dig = 0
    whi = 0
    rem = 0

    for line in fv:

        for c in line:
            if c.isalpha() and c.isupper():
                upp += 1
            elif c.isalpha() and c.islower():
                low += 1
            elif c.isdigit():
                dig += 1
            elif c.isspace():
                whi += 1
            else:
                rem += 1
    return upp, low, dig, whi, rem


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
    n = len(string)
    m = len(sub)
    i = 0

    if m > 0:
        while i <= n - m:
            if string[i:].startswith(sub):
                locations.append(i)
                # move to next possible sub
                i += m
            else:
                # move to next character
                i += 1
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
    if year % 400 == 0:
        leap_year = True
    elif year % 100 == 0:
        leap_year = False
    elif year % 4 == 0:
        leap_year = True
    else:
        leap_year = False
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

    if len(name) == 0:
        # name must be at least one character long
        valid = False
    elif not name[0].isalpha() and name[0] != '_':
        # Check first character for letters or underscore
        valid = False
    else:
        # Check rest of name for non-alphanumeric or '_'
        n = len(name)
        i = 1

        while valid and i < n:
            if not name[i].isalnum() and name[i] != '_':
                valid = False
            else:
                i += 1
    return valid


def matrix_transpose(a):
    """
    -------------------------------------------------------
    Transpose the contents of matrix a.
    a must be unchanged.
    Use: b = matrix_transpose(a):
    -------------------------------------------------------
    Parameters:
        a - a 2D list (2D list of int/float)
    Returns:
        b - the transposed matrix (2D list of int/float)
    -------------------------------------------------------
    """
    b = []
    rows = len(a)
    cols = len(a[0])

    for j in range(cols):
        row = []

        for i in range(rows):
            row.append(a[i][j])
        b.append(row)
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
    assert len(a) == len(b[0]) and len(a[0]) == len(b)

    c = []

    for i in range(len(a)):
        # for every row in a
        row = []

        for j in range(len(b[i])):
            # for every column in b
            total = 0

            for k in range(len(a[i])):
                # get dot product of row a column b
                total += a[i][k] * b[k][j]
            row.append(total)

        c.append(row)
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
    if len(word) > 0:
        if word[0] in VOWELS:
            # word begins with a vowel.
            pl = word + "way"
        else:
            if word[0].isupper():
                word = word[0].lower() + word[1:]
                upper = True
            else:
                upper = False
            # Find all consonants in front of string.
            # Treat "y" as a vowel in this case.
            i = 1

            while word[i] not in (VOWELS + "y"):
                i += 1
            # Construct the pig latin version of word.
            # Last part [i:] + first part [:i] + "ay".
            pl = word[i:] + word[:i] + "ay"

            if upper:
                pl = pl[0].upper() + pl[1:]
    else:
        pl = ""
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
    estring = ""

    for c in string:
        if c.isalpha():
            i = ALPHA.find(c.upper())
            i = (i + n) % ALPHA_SIZE
            estring += ALPHA[i]
        else:
            estring += c
    return estring
