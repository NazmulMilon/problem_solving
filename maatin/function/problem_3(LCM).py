def gcd(a, b):
    if b > a:
        gcd(b, a)
    while b != 0:
        temp = a%b
        a = b
        b = temp
    return a

def lcm(a, b):
    return (a*b)//gcd(a, b)

print("Please input two integers:")
a, b = map(int, input().split())
print(lcm(a, b))
