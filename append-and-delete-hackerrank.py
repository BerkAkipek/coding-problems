#!/usr/bin/python3

# Append and Delete Hackerrank

# You have two strings of lowercase English letters. 
# You can perform two types of operations on the first string:
# 1. Append a lowercase English letter to the end of the string.
# 2. Delete the last character of the string.
# Performing this operation on an empty string results in an empty string. 
# Given an integer, k, and two strings, s and t, 
# determine whether or not you can convert  to  by performing exactly  of the above operations on .

# Example
# s = [a, b, c]
# t = [d, e, f]
# k = 6
# To convert s to t, we first delete all of the characters in 3 moves.
# Next we add each of the characters of t in order.
# On the 6'th move, you will have the matching string. Return Yes.


def appendAndDelete(s, t, k):
    result = 0
    while len(s) != len(t):
        if len(s) > len(t):
            s = s.replace(s[-1], "")
            result += 1
    for i in range(len(s)-1, -1, -1):
        if s[i] == t[i]:
            pass
        else:
            result += 1
    if result <= k:
        return 'Yes'
    else:
        return 'No'




# This wont work we need to optimize this approach. Time limit exceeds. And it is wrong for two cases. 

def appendAndDelete(s, t, k):
    min_len = min(len(s), len(t))
    
    i = 0
    while s[i] == t[i]:
        i += 1
        if i == min_len:
            break
    
    diff = len(s) + len(t) - 2*i

    if len(s) + len(t) <= k:
        return 'Yes'
    elif diff > k:
        return 'No'
    else:
        if (k - diff) % 2 == 0:
            return 'Yes'
        else:
            return 'No'

print(appendAndDelete("hackerhappy", "hackerrank", 6))
print(appendAndDelete("hackerhappy", "hackerrank", 9))
