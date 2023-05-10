#!/usr/bin/python3

# Modified Kaprekar Numbers

# A modified Kaprekar number is a positive whole number with a special property.
# If you square it, then split the number into two integers and sum those integers, you have the same value you started with.
# Consider a positive whole number n with d digits.
# We square n to arrive at a number that is either 2xd digits long or (2xd) - 1 digits long.
# Split the string representation of the square into two parts, l and r.
# The right hand part, r must be d digits long. The left is the remaining substring.
# Convert those two substrings back to integers, add them and see if you get n.

# Example

# n = 5
# d = 1

# First calculate that n**2 = 25. Split that into two strings and convert them back to integers 2 and 5.
# Test (2 + 5) = 7 != 5, so this is not a modified Kaprekar number. 
# If n = 9, still d = 1, and n**2 = 81. This gives us 8 + 1 = 9, the original n.


# 1 9 45 55 99
example01 = 1
example02 = 45
example03 = 99
example04 = 64


def is_kaprekar_number(num):
    if num == 0:
        return False
    if num == 1:
        return True
    square = str(num * num)
    pivot = len(square) // 2
    left, right = int(square[:pivot] or 0), int(square[pivot:] or 0)
    if right != 0 and left + right == num:
        return True
    if int(square) == num:
        return True
    return False


def kaprekarNumbers(p, q):
    res = []
    for i in range(p, q+1):
        if is_kaprekar_number(i):
            res.append(i)
    if res:
        print(*res)
    else:
        print("INVALID RANGE")

kaprekarNumbers(1, 100)
