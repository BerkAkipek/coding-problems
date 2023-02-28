#!/usr/bin/python3

# Sherlock And Squares 

# Watson likes to challenge Sherlock's math ability.
# He will provide a starting and ending value that describe a range of integers, inclusive of the endpoints.
# Sherlock must determine the number of square integers within that range.
# Note: A square integer is an integer which is the square of an integer, e.g.

# Example 
# a = 24
# b = 49
# returns 3 bacause of 25, 36, 49


import math


def squares(a, b):
    result = 0
    for i in range(a, b+1):
        for j in range(i):
            if j*j > i:
                break
            elif j*j == i:
                result += 1
    return result

# First answer has O(n*j) complexity time limit exceeded

def squares(a, b):
    result = 0
    i = math.ceil(math.sqrt(a))
    for j in range(i, b+1):
        if j*j > (b+1):
            break
        result += 1
    return result

# This is a better answer with O(sqrt(n)) complexity


def squares(a, b):
    count = math.floor(math.sqrt(b)) - math.ceil(math.sqrt(a)) + 1
    return count

# This answer is the best has O(1) complexity

