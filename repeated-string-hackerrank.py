#!/usr/bin/python3

# Repeated String Hackerrank

# There is a string, s, of lowercase English letters that is repeated infinitely many times.
# Given an integer, n, find and print the number of letter a's in the first n letters of the infinite string.

# Example
# s = 'abcac'
# n = 10
# s = abcacabcac in this repeated string there is 4 a's exist. return 4

# Example 
# s = 'aba'
# n = 10
# string = aba aba aba a... return 7

def repeatedString(s, n):
    length = len(s)

    count = 0
    for char in s:
        if char == 'a':
            count += 1
    
    residual = 0
    if n % length == 0:
        return ((n // length) * count)
    else:
        for i in range(n % length):
            if s[i] == 'a':
                residual += 1
        return (((n // length) * count) + residual)

if __name__ == '__main__':
    print(repeatedString('abcac', 10))
    print(repeatedString('aba', 10))
