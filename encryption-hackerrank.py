#!/usr/bin/python3

# Encryption Hackerrank

# An English text needs to be encrypted using the following encryption scheme.
# First, the spaces are removed from the text. Let L be the length of this text.
# Then, characters are written into a grid, whose rows and columns have the following constraints:

# \L/ <= row <= column <= /L\ 

# Where \a/ and /a\ are floor and ceil respectively. 

# Example

# s = "If man was meant to stay on the ground god would have given us roots"
# After removing spaces, the string is 54 characters long. sqrt(54) is between 7 and 8, so it is written in the form of a grid with 7 rows and 8 columns.
# Ensure that rows * columns = L
# If multiple grids satisfy the above conditions, choose the one with the minimum area, i.e. rows * columns.

# ifmanwas  
# meanttos          
# tayonthe  
# groundgo  
# dwouldha  
# vegivenu  
# sroots

# The encoded message is obtained by displaying the characters of each column, with a space between column texts. The encoded message for the grid above is:
# imtgdvs fearwer mayoogo anouuio ntnnlvt wttddes aohghn sseoau

import math

example01 = "if man was meant to stay on the ground god would have given us roots"
example02 = "haveaniceday"
example03 = "feedthedog"
example04 = "chillout"


def encryption(s):
    # TODO 1: Remove Spaces
    s = s.replace(" ", "")
    # TODO 2: Calculate sides of the grid
    rows, columns = math.floor(math.sqrt(len(s))), math.ceil(math.sqrt(len(s)))
    if rows * columns >= len(s):
        pass
    else:
        rows = columns
    # TODO 3: Generate the Grid
    grid = []
    for i in range(rows):
        row = []
        for elem in s[(i*columns):(i*columns) + columns]:
            row.append(elem)
        grid.append(row)
    # TODO 4: Complete the matrix for encryption
    rslt = ""
    for i in range(len(grid[0])):
        for j in range(len(grid)):
            try:
                rslt += grid[j][i]
            except:
                pass
        rslt += " "
    return rslt

print(encryption(example01))
print(encryption(example02))
print(encryption(example03))
print(encryption(example04))