a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
mul=a*b

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

lcm=mul//a
print("LCM is: ",  lcm)



'''def compute_lcm(x, y):
    # choose the greater number
    if x > y:
       greater = x
    else:
       greater = y

    while(True):
        if (greater % x == 0) and (greater % y == 0):
            lcm = greater
            break
        greater += 1
    return lcm


num1 = 54
num2 = 24
print("The L.C.M. is", compute_lcm(num1, num2))
'''