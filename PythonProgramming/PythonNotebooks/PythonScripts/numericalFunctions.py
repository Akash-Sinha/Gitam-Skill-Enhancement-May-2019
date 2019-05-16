def factorial(n):
    if n == 1 or n == 0:
        return 1
    return factorial(n-1) * n


def sumN(n):
    if n == 1:
        return 1
    return sumN(n-1) + n


#print(factorial(9))