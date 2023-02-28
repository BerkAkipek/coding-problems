#!/usr/bin/python3

# Library Fine Hackerrank

# Your local library needs your help!
# Given the expected and actual return dates for a library book, create a program that calculates the fine (if any).
# The fee structure is as follows:
# 1. If the book is returned on or before the expected return date, no fine will be charged (i.e.: fine = 0).
# 2. If the book is returned after the expected return day but still within the same calendar month and year as the expected return date,
# fine = 15 Hackos * (number of days late)
# 3. If the book is returned after the expected return month but still within the same calendar year as the expected return date, the
# fine = 500 Hackos * (number of months late)
# 4. If the book is returned after the calendar year in which it was expected, there is a fixed fine of 10000 Hackos.

# Charges are based only on the least precise measure of lateness. 
# For example, whether a book is due January 1, 2017 or December 31, 2017, if it is returned January 1, 2018, 
# that is a year late and the fine would be 10000 Hackos.

# Example 
# d1, m1, y1 = 14, 7, 2018
# d2, m2, y2 = 5, 7, 2018
# The first values are the return date and the second are the due date.
# The years are the same and the months are the same.
# The book is 14 - 5 = 9 days late. Return 15 * 9 = 135 Hackos.

# PseudoCode:
# 1. Look for years if it is not matched return 10000. 
# 2. Look for the months if it's not matches return diff * 500
# 3. Look for the day if it's not matched return diff * 15

def libraryFine(d1, m1, y1, d2, m2, y2):
    if y1 > y2:
        return 10000
    else:
        if m1 > m2:
            return 500 * (m1 - m2)
        else:
            if d1 > d2:
                return 15 * (d1 - d2)
            else:
                return 0


# This solution calculate fine correctly but it fails if customer give their book on time. 
# I need to change my pseudocode and algorithm. 

# PseudoCode:
# 1. Look for years if it is not matched return 10000. 
# 2. Look for the months if it's not matches return diff * 500
# 3. Look for the day if it's not matched return diff * 15

print(libraryFine(28, 2, 2015, 15, 4, 2015))

# It fails because we dont consider early year and early month situation. 
# This is correct version

def libraryFine(d1, m1, y1, d2, m2, y2):
    if y1 > y2:
        return 10000
    elif y1 < y2:
        return 0
    else:
        if m1 > m2:
            return 500 * (m1 - m2)
        elif m1 < m2:
            return 0
        else:
            if d1 > d2:
                return 15 * (d1 - d2)
            else:
                return 0

