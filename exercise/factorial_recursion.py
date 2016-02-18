def factorial(x):
    while x > 1:
        return x * factorial(x-1)
    else:
        return 1