
n = int(input())
result = 0
count = 0
for i in range(1, n+1):
    print("Enter ", i, ":", end="")
    a,b,c = map(int(input().split()))

    result = a+b+c
    if result>=2:
        count=count+1
print(count)
