#!/usr/bin/python3

# Jumping On The Clouds Hackerrank 

# There is a new mobile game that starts with consecutively numbered clouds.
# Some of the clouds are thunderheads and others are cumulus.
# The player can jump on any cumulus cloud having a number that is equal to the number of the current cloud plus 1 or 2.
# The player must avoid the thunderheads.
# Determine the minimum number of jumps it will take to jump from the starting postion to the last cloud.
# It is always possible to win the game.

# For each game, you will get an array of clouds numbered 0 if they are safe or 1 if they must be avoided.

# Example
# c = [0, 1, 0, 0, 0, 1, 0]
# There is only possible 2 ways. 
# Because i can't jump clouds 1 and 5 indexed.  
# 0 -> 2 -> 4 -> 6 | 0 -> 2 -> 3 -> 4 -> 6 

# Pseudocode 
# Start jumping with a length of two 
# if you land a thunder cloud reduce index by 1
# Count if jump was valid

def jumpingOnClouds(c):
    count = 0
    for i in range(0, len(c), 2):
        if c[i] == 1:
            i -= 3
            continue
        else:
            print(i, end=' ')
            count += 1
    return count

# This approach is so wrong we are starting counting from first cloud. 
# Even expected values wrong. 

def jumpingOnClouds(c):
    result = 0
    i = 0
    while i < len(c) - 1:
        if (i + 2) < len(c) and c[i + 2] == 0:
            i += 2
            result += 1
        else:
            i += 1
            result += 1
    return result


if __name__ == '__main__':
    print(jumpingOnClouds([0, 0, 0, 1, 0, 0])) # Expected: 3
    print(jumpingOnClouds([0, 0, 1, 0, 0, 1, 0])) # Expected 4