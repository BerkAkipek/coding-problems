# Utopian Tree By Hackerrank

# The Utopian Tree goes through 2 cycles of growth every year.
# Each spring, it doubles in height. Each summer, its height increases by 1 meter.
# A Utopian Tree sapling with a height of 1 meter is planted at the onset of spring.
# How tall will the tree be after n'th growth cycles?

# For example, if the number of growth cycles is n=5, the calculations are as follows:
# Period  Height
# 0          1
# 1          2
# 2          3
# 3          6
# 4          7
# 5          14

def utopianTree(n):
    height = 1
    
    for i in range(1, n+1):
        if i % 2 == 0:
            height += 1
        else:
            height *= 2
    
    return height

if __name__ == '__main__':
    print(utopianTree(5))
