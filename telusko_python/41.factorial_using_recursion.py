

n = int(input("Enter a number: "))


def factorial(n):

    if n == 0:
        return 1

    result = n*factorial(n-1)
    return result


factorial(n)
print(factorial(n))










'''n=int(input("Enter a number of factorial: "))


def recursion(n):

    if n == 0:
        return 1

    return n*recursion(n-1)


recursion(n)
print(recursion(n))'''
