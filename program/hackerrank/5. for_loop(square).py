n=int(input("Enter a number:"))

print(*[num**2 for num in range(n)], sep='\n')

'''for i in range(0,n):
    print(i*i)
'''
'''
for i in range(0,n):
    print pow(i,2)
'''