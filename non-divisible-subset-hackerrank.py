#!/usr/bin/python3

# Non-Divisible Subset Hackerrank

# Given a set of distinct integers, print the size of a maximal subset of S 
# where the sum of any 2 numbers in S' is not evenly divisible by k.

# Example
# S = [19, 10, 12, 10, 24, 25, 22]; k = 4
# One of the arrays that can be created is S'[0] = [10, 12, 25]. 
# Another is S'[1] = [19, 22, 24]. After testing all permutations, the maximum length solution array has 3 elements.

# Pseudo Code
# for each element in arr
# found subset's meets criteria 
# Create a list of lengths append length of every subset to list 
# return max of lenghts list

def nonDivisibleSubset(k, s):
    subset_len = []
    for elem1 in s:
        subset = []
        for elem2 in s:
            if (elem1 + elem2) % k == 0:
                subset.append(elem2)
        subset.append(elem1)
        subset_len.append(len(subset))
    return max(subset_len)


def nonDivisibleSubset(k, s):
    subset01, subset02 = [], []
    for elem in s:
        if (elem % k) <= (k // 2):
            subset01.append(elem)
        else:
            subset02.append(elem)
    return max(len(subset01), len(subset02))


# This attempts did not worked

# PseudoCode
# 1. Create an array to store the remainder count for each number
# 2. Initialize the max subset size
# 3. If there is a remaninder of 0, we can include only one number
# 4. If k is even, we can add only one number with remainder k/2
# 5. Add max of remainder counts for each i and k-i pairs

def nonDivisibleSubset(k, s):
    remainder_arr = [0] * k

    for num in s:
        remainder_arr[num%k] += 1
    
    max_subset_size = 0

    if remainder_arr[0] > 0:
        max_subset_size += 1
    
    if k%2 == 0 and remainder_arr[k//2] > 0:
        max_subset_size += 1
    
    for i in range(1, (k+1)//2):
        max_subset_size += max(remainder_arr[i], remainder_arr[k-i])
    
    return max_subset_size


s = [1, 7, 2, 4]
k = 3

print(nonDivisibleSubset(k, s))

s = [278, 576, 496, 727, 410, 124, 338, 149, 209, 702, 282, 718, 771, 575, 436]
k = 7

print(nonDivisibleSubset(k, s))
