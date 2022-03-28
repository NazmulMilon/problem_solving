print("Please input three integers:")
#a, b, c=input().split()
a,b,c= map(int, input().split())

if a >= b and a >= c:
    greatest = a
elif b >= a and b >= c:
    greatest = b
else:
    greatest = c

print(greatest)