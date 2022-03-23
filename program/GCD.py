a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
if b>a:
    a,b = b,a # make swaping

while a!=b:
    if b ==0:
        break
    if a>b:
        a=a-b
    else:
        b=b-a
print("GCD is: ", a)