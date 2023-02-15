# Hackerrank Forming a Magic square

# For a magic square all possile reflections and reflections of it's transposition also a magic square. 
# This makes 8 possible magic squares. Let's write them as a 3 dimensional matrix.

allMagicSquares = [
        [[8, 1, 6], [3, 5, 7], [4, 9, 2]], 
        [[6, 1, 8], [7, 5, 3], [2, 9, 4]], 
        [[4, 9, 2], [3, 5, 7], [8, 1, 6]], 
        [[2, 9, 4], [7, 5, 3], [6, 1, 8]], 
        [[8, 3, 4], [1, 5, 9], [6, 7, 2]], 
        [[4, 3, 8], [9, 5, 1], [2, 7, 6]], 
        [[6, 7, 2], [1, 5, 9], [8, 3, 4]], 
        [[2, 7, 6], [9, 5, 1], [4, 3, 8]]]

# Calculate the linear distance for each dot to corresponding dot in all magic square. 
# Return the minimum of distances. 

def formingMagicSquare(s):
    cost = 0
    collection = []
    for i in range(len(allMagicSquares)):
        current = allMagicSquares[i] # current 2D
        for j in range(len(current)):
            for k in range(len(current[j])):
                cost += abs(current[j][k] - s[j][k])
        collection.append(cost)
        cost = 0
    return min(collection)

