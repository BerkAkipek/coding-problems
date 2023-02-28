#/usr/bin/python3

# Cut The Sticks Hackerrank

# You are given a number of sticks of varying lengths.
# You will iteratively cut the sticks into smaller sticks, discarding the shortest pieces until there are none left.
# At each iteration you will determine the length of the shortest stick remaining,
# cut that length from each of the longer sticks and then discard all the pieces of that shortest length.
# When all the remaining sticks are the same length, they cannot be shortened so discard them.

# Given the lengths of n sticks, print the number of sticks that are left before each iteration until there are none left.

# Example 
# arr = [1, 2, 3]
# The shortest stick length is 1, so cut that length from the longer two and discard the pieces of length 1.
# Now the lengths are arr = [1, 2].
# Again, the shortest stick is of length 1, so cut that amount from the longer stick and discard those pieces.
# There is only one stick left, arr = [1], so discard that stick.
# The number of sticks at each iteration are answer = [3, 2, 1].


def cutTheSticks(arr):
    answer = [len(arr)]
    while len(arr) != 0:
        i = 0
        for _ in arr:
            cut_len = min(arr)
            arr[i] = arr[i] - cut_len
            if arr[i] == 0:
                arr.remove(arr[i])
            i += 1
        answer.append(len(arr))
    return answer

# This solution did not worked. 
# But a do while loop can work i will do it with an infinite loop. 

def cutTheSticks(arr):
    answer = []
    while True:
        answer.append(len(arr))
        shortest = min(arr)
        i = 0
        while i < len(arr):
            arr[i] = arr[i] - shortest
            if arr[i] == 0:
                arr.remove(arr[i])
                i -= 1
            i += 1
        if len(arr) == 0:
            break
    return answer


print(cutTheSticks([5, 4, 4, 2, 2, 8]))
print(cutTheSticks([1, 2, 3, 4, 3, 3, 2, 1]))
