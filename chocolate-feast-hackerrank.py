#!/usr/bin/python3

# Chocolate Feast Hackerrank

# Little Bobby loves chocolate. He frequently goes to his favorite 5 & 10 store, Penny Auntie, to buy them.
# They are having a promotion at Penny Auntie.
# If Bobby saves enough wrappers, he can turn them in for a free chocolate.

# Example

# n = 15
# c = 3
# m = 2

# He has 15 to spend, bars cost 3, and he can turn in 2 wrappers to receive another bar.
# Initially, he buys 5 bars and has 5 wrappers after eating them.
# He turns in 4 of them, leaving him with 1, for 2 more bars.
# After eating those two, he has 3 wrappers, turns in 2 leaving him with 1 wrapper and his new bar.
# Once he eats that one, he has 2 wrappers and turns them in for another bar.
# After eating that one, he only has  wrapper, and his feast ends.
# Overall, he has eaten (5 + 2 + 1 + 1) = 9 bars.

example1 = (15, 3, 2) # -> 9
example2 = (7, 3, 2) # -> 3
example3 = (10, 2, 5) # -> 6

def chocolateFeast(n, c, m):

    total_bars = wrappers = n//c
    
    #if number of wrappers is less than wrappers required for a free bar, the feast has to end.
    while wrappers >= m:
        new_bars = wrappers // m
        wrappers = wrappers % m + new_bars
        total_bars += new_bars
        
    return total_bars


def main():
    print(chocolateFeast(15, 3, 2))
    print(chocolateFeast(7, 3, 2))
    print(chocolateFeast(10, 2, 5))


if __name__ == '__main__':
    main()
