#/usr/bin/python3

# Halloween Sale Hackerrank

# You wish to buy video games from the famous online video game store Mist.
# Usually, all games are sold at the same price, p dollars.
# However, they are planning to have the seasonal Halloween Sale next month in which you can buy games at a cheaper price.
# Specifically, the first game will cost p dollars, and every subsequent game will cost d dollars less than the previous one.
# This continues until the cost becomes less than or equal to m dollars, after which every game will cost m dollars.
# How many games can you buy during the Halloween Sale?

# Example

# p = 20
# d = 3
# m = 6
# s = 70

# The following are the costs of the first 9, in order:
# 20 -> 17 -> 14 -> 11 -> 8 -> 6 -> 6 -> 6 -> 6
# Start at p = 20 units cost, reduce that by d = 3 units each iteration until reaching a minimum possible price, m = 6.
# Starting with s = 70 units of currency in your Mist wallet, you can buy 5 games: (20 + 17 + 14 + 11 + 8) = 70.


def howManyGames(p, d, m, s):
    count = 0
    while s >= p:
        s = s - p
        count += 1
        p = max(m, p-d)
    return count


print(howManyGames(20, 3, 6, 70))
print(howManyGames(16, 2, 1, 9981)) # -> 9917
print(howManyGames(99, 3, 1, 5555))
print(howManyGames(13, 86, 8, 9027)) # -> 1127 