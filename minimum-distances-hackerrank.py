#!/usr/bin/python3

# Minimum Distances Hackerrank 

# The distance between two array values is the number of indices between them.
# Given a, find the minimum distance between any pair of equal elements in the array.
# If no such value exists, return -1.

# Example

# a = [3, 2, 1, 2, 3]
# There are two matching pairs of values: 3 and 2.
# The indices of the 3's are i=0 and j=4, so their distance is d[i, j] = |j - i| = 4.
# The indices of the 2's are i=1 and j=3, so their distance is d[i, j] = |j - i| = 2. 
# The minimum distance is 2.


def minimumDistances(a):
    d = 0
    for i in range(len(a) - 1):
        for j in range(i+1, len(a)):
            if a[i] == a[j]:
                if d == 0:
                    d = abs(j - i)
                elif d > abs(j - i):
                    d = abs(j - i)
    if d == 0:
        return -1
    return d


def main():
    example1 = [7, 1, 3, 4, 1, 7]
    example2 = [1, 2, 3, 4, 10]
    example3 = [3, 2, 1, 2, 3]
    print(minimumDistances(example1))
    print(minimumDistances(example2))
    print(minimumDistances(example3))


if __name__ == '__main__':
    main()
