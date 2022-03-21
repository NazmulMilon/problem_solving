import math

while True:
    n = int(input(" Enter a positive integer. Enter 0 to quit: "))
    if n==0:
        break
    if n<0:
        print("You must enter a positive integer. Please try again")

    factors=[1, n]
    sqrt_n=math.sqrt(n)
    sqrt_n = int(sqrt_n)

    for i in range(2, sqrt_n+1):
        if n%i==0:
            factors.append(i)
            factors.append(n//i)

    factors = sorted(factors)
    print("factors of", n, ":", factors)
    print("\n")


'''while True:
    n = input("Enter a positive integer. Enter 0 to quit: ")
    n=int(n)
    if n == 0:
        break
    if n < 0:
        print("You must enter a positive integer. Please try again.")
        continue

    factors = [1, n]

    for i in range(2, (n//2)+1):
        if n%i == 0:
            factors.append(i)

    factors = sorted(factors)
    print("Factors of", n, ":", factors)
    print("\n")
    '''
