

n = int(input())

count = 0
i=0

while n > 0:
    mod = n%10

    #print(mod)
    n = n//10

    if mod == 4 or mod == 7:
        count += 1

    i += 1

if count==4 or count ==7:
    print("YES")
else:
    print("NO")