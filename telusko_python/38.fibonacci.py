n = int(input("Enter a number: "))


def fibonacci(n):
    a=0
    b=1
    if n == 1:
        print(a)
    else:
        print(a, end=" ")
        print(b, end=" ")

        for i in range(2, n):
            c = a + b
            print(c, end=" ")
            a = b
            b = c


fibonacci(n)


'''n = int(input("Enter a number: "))

def fibonacci(n):
    a=0
    b=1
    print(a, end=" ")
    print(b, end=" ")

    for i in range(2, n):
        c=a+b
        print(c, end=" ")
        a=b
        b=c


fibonacci(n)
'''
'''n = int(input("Enter number: "))

a=0
b=1
print(a, end=" ")
print(b, end=" ")

for i in range(3, n+1):
    c= a+b
    # print(c, end=" ")

    a=b
    b=c


    print(c, end=" ")'''
