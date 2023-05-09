#!/usr/bin/python3

# Bigger is Greater Hackerrank

# Lexicographical order is often known as alphabetical order when dealing with strings.
# A string is greater than another string if it comes later in a lexicographically sorted list.

# Given a word, create a new word by swapping some or all of its characters. This new word must meet two criteria:
# 1. It must be greater than the original word
# 2. It must be the smallest word that meets the first condition

# Example

# w = "abcd"
# Next largest word is "abdc"

# Complete the function biggerIsGreater below to create and return the new string meeting the criteria. If it is not possible, return no answer.

example1 = "ab"
example2 = "lmno"
example3 = "abcd"


def biggerIsGreater(w):
    for i in range(len(w) - 1, 0, -1):
        if w[i] > w[i-1]:
            s = sorted(w[i-1:])
            c = ''
            for j in s:
                if j > w[i-1]:
                    c = j
                    s.remove(j)
                    break
            rep = ''.join(sorted(s))
            b = w[:i-1]+c+rep
            return b
    return "no answer"


print(biggerIsGreater(example1))
print(biggerIsGreater(example2))
print(biggerIsGreater(example3))