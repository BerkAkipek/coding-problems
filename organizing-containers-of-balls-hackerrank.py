#!/usr/bin/python3

# Organizing Containers Of Balls Hackerrank

# David has several containers, each with a number of balls in it. 
# He has just enough containers to sort each type of ball he has into its own container.
# David wants to sort the balls using his sort method.
# Each container contains only balls of the same type.
# No two balls of the same type are located in different containers.

# Example
# containers = [[1, 4], [2, 3]]
# David has n = 2 containers and 2 different types of balls, both of which are numbered from 0 to n-1 = 1.
# The distribution of ball types per container are shown in the following diagram.

# In a single operation, David can swap two balls located in different containers.
# The diagram below depicts a single swap operation:

# In this case, there is no way to have all green balls in one container and all red in the other using only swap operations. Return Impossible.

container01 = [[1, 1], [1, 1]]
container02 = [[1, 3, 1], [2, 1, 2], [3, 3, 3]]


def organizingContainers(container):
    ball_counts = [0] * len(container) # [0 0], [0 0 0]
    poss = "Possible"
    for i in range(len(container)):
        ball_counts[i] += sum([container[j][i] for j in range(len(container))]) # Elementwise sum of lists
    for i in range(len(container)):
        if sum(container[i]) not in ball_counts:
            poss = "Impossible"
            break
    return poss


print(organizingContainers(container=container01))
print(organizingContainers(container=container02))
