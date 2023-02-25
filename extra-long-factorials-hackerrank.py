# Extra Long Factorials Hackerrank

# The factorial of the integer n, written n!, is defined as:
# n! = n * (n-1) * (n-2) * ... * 2 * 1

# Calculate and print the factorial of a given integer.

def extraLongFactorials(n):
    result = 1
    for i in range(2, n+1):
        result *= i
    print(result)

