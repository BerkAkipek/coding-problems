#!/usr/bin/python3

# Equalize The Array Hackerrank

# Given an array of integers, 
# determine the minimum number of elements to delete to leave only elements of equal value.

# Example 
# arr = [1, 2, 2, 3]
# Delete the  elements 1 and 3 leaving [2, 2]. 
# If both twos plus either the 1 or the 3 are deleted, it takes 3 deletions to leave either [1] or [3]. 
# The minimum number of deletions is 2.

# Pseudocode
# First found most frequent item in that list 
# Count each element which is not equal to most frequent. 
# Return counted number. 


def mostFrequent(arr):
    counter = 0
    num = arr[0]

    for i in arr:
        curr_frequency = arr.count(i)
        if curr_frequency > counter:
            counter = curr_frequency
            num = i
    
    return num


def equalizeArray(arr):
    most = mostFrequent(arr)
    counter = 0

    for i in range(len(arr)):
        if arr[i] != most:
            counter += 1
    
    return counter

