# Circular Array Rotation Hackerrank

# John Watson knows of an operation called a right circular rotation on an array of integers.
# One rotation operation moves the last array element to the first position and shifts all remaining elements right one.
# To test Sherlock's abilities, Watson provides Sherlock with an array of integers.
# Sherlock is to perform the rotation operation a number of times then determine the value of the element at a given position.
# For each array, perform a number of right circular rotations and return the values of the elements at the given indices.

# Example
# a = [3, 4, 5]
# k = 2
# queries = [1, 2]

# Here k is the number of rotations on a, and queries holds the list of indices to report.
# First we perform the two rotations: [3, 4, 5] -> [5, 3, 4] -> [4, 5, 3]

# Now return the values from the zero-based indices 1 and 2 as indicated in the queries array.
# a[1] = 5
# a[2] = 3

# Function Description
# Complete the circularArrayRotation function in the editor below.
# circularArrayRotation has the following parameter(s):

# int a[n] array to rotate
# int k rotation count 
# int queries[1] the indices to report

# Returns

# int[q]: the values in the rotated a as requested in m


def rightCircularRotation(arr, n):
    for i in range(0, n):
        last = arr[len(arr) - 1]
        for j in range(len(arr) - 1, -1, -1):
            arr[j] = arr[j-1]
        arr[0] = last
    return arr


def circularArrayRotation(a, k, queries):
    arr = rightCircularRotation(a, k)
    result = []
    for query in queries:
        result.append(arr[query])
    return result


# Solution above loops through all elements in array k times 
# It has O(n*k) computations
# Thats why execution time limit exceed 
# we are going with this solution


def circularArrayRotation(a, k, queries):
    numLists = list(a)
    for i in range(k):
        numLists.insert(0, numLists.pop())
    return [numLists[i] for i in queries]

