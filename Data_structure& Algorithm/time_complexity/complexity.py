
'''a=1
b=3
for i in range(a, b+1):
    print(i)'''

# Time Complexity== O(n*n)

n=int(input("Enter a number:"))
count=0
for i in range(0,n):
    for j in range(0,n):
        count=count+1

print(n, count)
