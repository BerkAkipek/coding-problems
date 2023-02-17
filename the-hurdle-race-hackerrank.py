# The Hurdle Race Hackerrank 

# A video player plays a game in which the character competes in a hurdle race.
# Hurdles are of varying heights, and the characters have a maximum height they can jump.
# There is a magic potion they can take that will increase their maximum jump height by 1 unit for each dose.
# How many doses of the potion must the character take to be able to jump all of the hurdles.
# If the character can already clear all of the hurdles, return 0.

# Example
# height = [1, 2, 3, 3, 2]
# k = 1
# Character must take |3 - 1| = 2 potions

def hurdleRace(k, height):
    potion = 0
    for hurdle in height:
        if hurdle > k:
            potion += (hurdle - k)
            k = hurdle
    return potion


if __name__ == '__main__':
    print(hurdleRace(1, [1, 2, 3, 3, 2]))
