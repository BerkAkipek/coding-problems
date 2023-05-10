#!/usr/bin/python3

# Beautiful Triplets Hackerrank

# Given a sequence of integers a, a triplet (a[i], a[j], a[k]) is beautiful if:
# i < j < k
# a[j] - a[i] == a[k] - a[j] == d
# Given an increasing sequence of integers and the value of d, count the number of beautiful triplets in the sequence.

# Example

# arr = [2, 2, 3, 4, 5]
# d = 1
# There are three beautiful triplets, by index: [i, j ,k] = [0, 2, 3], [1, 2, 3], [2, 3, 4]
# To test the first triplet,  and .

def beautifulTriplets(d, arr):
    rslt = 0
    for i in arr:
        if (i + d) in arr and (i + 2*d) in arr:
            rslt += 1
    return rslt

