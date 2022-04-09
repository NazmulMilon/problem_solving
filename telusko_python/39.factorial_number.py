
n = int(input("Enter a number: "))


def factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact = fact*i
    # print("Result is: ", fact)
    return fact


factorial(n)
print(factorial(n))

'''n = int(input("Enter a number: "))
fact = 1
for i in range(1, n+1):
    fact = fact*i
print("Factorial of" , n ,"is:", fact)'''