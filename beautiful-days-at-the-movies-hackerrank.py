# Beautiful Days At The Movies Hackerrank

# Lily likes to play games with integers.
# She has created a new game where she determines the difference between a number and its reverse.
# For instance, given the number 12, its reverse is 21. Their difference is 9.
# The number 120 reversed is 21, and their difference is 99.

# She decides to apply her game to decision making. 
# She will look at a numbered range of days and will only go to a movie on a beautiful day.
# Given a range of numbered days, [i...j] and a number k, determine the number of days in the range that are beautiful.
# Beautiful numbers are defined as numbers where |i - reverse(i)| is evenly divisible by k.
# If a day's value is a beautiful number, it is a beautiful day. Return the number of beautiful days in the range.

# Function Description
# Complete the beautifulDays function in the editor below.
# beautifulDays has the following parameter(s):
# # int i: the starting day number
# # int j: the ending day number
# # int k: the divisor
# Returns
# # int: the number of beautiful days in the range


def reverseNumber(number):
    reversedNum = 0
    while number != 0:
        digit = number % 10
        reversedNum = reversedNum * 10 + digit
        number //= 10
    return reversedNum

def beautifulDays(i, j, k):
    days = [day for day in range(i, j+1)]
    result = 0
    for day in days:
        if abs(day - reverseNumber(day)) % k == 0:
            result += 1
    return result


if __name__ == '__main__':
    print(beautifulDays(1, 24, 6))
