from array import *

arr = array('i',[])

n = int(input("Enter the range of numbers: "))

for i in range(n):
    x = int(input("Enter the next value: "))
    arr.append(x)
    i=i+1
print(arr)

s = int(input("Entr the search number: "))

k=0
for e in arr:
    if e == s:
        print(k)
        break
    k+=1

print(arr.index(s))











'''arr = array('i', [])

n = int(input("Enter the length of the array:"))

for i in range(n):
    x = int(input("Enter the next value: "))
    arr.append(x)
print(arr)


val = int(input("Enter the value for search: "))
k=0
for e in arr:
    if e==val:
        print(k)
        break

    k+=1

print(arr.index(val))
'''