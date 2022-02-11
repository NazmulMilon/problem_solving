#Time Complexity== O(n*n + n)= O(n*n) or square of n


n=int(input("Enter a number:"))

count=0
for i in range(0,n):
    for j in range(0,n):
        count=count+1

for i in range(0,n):
    count=count+1

print(count)
