
# Hackerrank Picking Numbers

# Given an array of integers, 
# find the longest subarray where the absolute difference between 
# any two elements is less than or equal to 1.

#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def pickingNumbers(a):
    collection, max_val = 0, 0
    a.sort()
    for i in range(len(a) - 1):
        for j in range(i, len(a)):
            if a[j] - a[i] <= 1:
                collection += 1
                if collection > max_val:
                    max_val = collection
        collection = 0
    return max_val

