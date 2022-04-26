

a,b,c = map(int, input().split())

if (a==b and a==c) or (a!=b and b!=c):
    print("No")
elif(a==b and a!=c) or (a==c and a!=b) or (b==c and b!=a) or (b==a and b!=c) or (c==a and c!=b) or (c==b and c!=a):
    print("Yes")