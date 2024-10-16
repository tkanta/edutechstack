def factorial(n):
    # Base case
    if n == 0 or n == 1:
        return 1
    if n < 0:
        return -1
    return n * factorial(n - 1)


print(factorial(8))
