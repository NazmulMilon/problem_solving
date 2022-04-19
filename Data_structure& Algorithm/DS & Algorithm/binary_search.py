lst =[]
n= int(input("Enter the range: "))

for i in range(n):
    item = int(input("Enter the number: "))
    lst.append(item)

r = int(input("Finding number: "))

def binary_search(lst, r):
    lower = 0
    upper =len(lst)-1
    mid = (lower+upper)//2

    for i in range(len(lst)):
        if lst[i]==r:
            return i
        elif lst[i]>r:
            upper = mid-1
        else:
            lower = mid+1


result = binary_search(lst, r)

if result==-1:
    print("Not Found")

else:
    print("Found at: ", result+1)

'''n = int(input("Enter the range: "))
e = list(map(int, input("Enter the items: ").split()))[:n]
r = int(input("Enter finding item: "))


def binary_search(e, r):
    lower = 0
    upper = len(e)-1
    mid = (lower+upper)//2

    for i in range(len(e)):
        if e[i] == r:
            return i
        elif e[i]>r:
            upper = mid-1
        else:
            lower = mid+1
    else:
        return -1


result = binary_search(e, r)

if result== -1:
    print("Not Found the number: ", r)
else:
    print("The item found at: ", result+1)
'''


'''lst = [11, 22, 33, 44, 55]
r = 33


def binary_search(lst, r):
    lower = 0
    upper = len(lst) - 1
    mid = (lower + upper) // 2
    for i in range(len(lst)):
        if lst[i] == r:
            return i

        elif lst[i] > r:
            upper = mid-1
        else:
            lower = mid+1
    else:
        return -1


index = binary_search(lst, r)

if index == -1:
    print("Not Found")
else:
    print("Found at: ", index+1)
'''



'''pos=-1

def binary_search(list, n):
    l=0
    u=len(list)-1
    while l<=u:
        mid=(l+u)//2
        if list[mid]==n:
            globals()['pos']=mid
            return True
        else:
            if list[mid]<n:
                l=mid+1
            else:
                u=mid-1
    return False

list = [5, 4, 9, 12, 44, 55]
n=55

if binary_search(list, n):
    print("Found at: ", pos+1)
else:
    print("Not found")
'''