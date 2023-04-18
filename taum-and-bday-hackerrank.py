#!/usr/bin/python3

# Taum And B'day Hackerrank

# Taum is planning to celebrate the birthday of his friend, Diksha.
# There are two types of gifts that Diksha wants from Taum: one is black and the other is white.
# To make her happy, Taum has to buy b black gifts and w white gifts.
# The cost of each black gift is bc units.
# The cost of every white gift is wc units.
# The cost to convert a black gift into white gift or vice versa is z units.

# Determine the minimum cost of Diksha's gifts.

def taumBday(b, w, bc, wc, z):
    if (bc + z) < wc or (wc + z) < bc:
        if bc < wc:
            total = (b * bc) + (w * (bc + z))
        else:
            total = (w * wc) + (b * (wc + z))
    else:
        total = b * bc + w * wc
    return total

