a, b = map(int, input().split())


'''c = a + b
d = a - b
e = a * b
#print( c,"\n",d,"\n",e)
print("%d\n%d\n%d"%(c,d,e))
'''
# print(f"{a+b}\n{a-b}\n{a*b}")
# (lambda a, b : print((a + b), (a - b), (a * b), sep="\n"))(int(input()), int(input()))
'''a,b = int(input()), int(input())
print(*[a+b, a-b, a*b], sep="\n")'''

print(a+b)
print(a-b)
print(a*b)