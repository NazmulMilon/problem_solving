
# linear search function


def linear_search(arr, n, item):
    for i in range(0, n):
        if arr[i]==item:
            return i
    else:
        return -1


arr=[]
n = int(input("Enter the size of array: "))

for i in range(0, n):
    a = int(input("Elements of array: "))
    arr.append(a)

item = int(input("Enter the index number: "))


index = linear_search(arr, n, item)
if index == -1:
    print("Array Not Found")

else:
    print("Number found at: ", index+1)




'''pos=-1
def search(list, n):
    i=0
    while i<len(list):
        if list[i]==n:
            globals()['pos']=i
            return True
        i=i+1
    return False


list = [5,6,9,75,88]
n=75

if search(list, n):
    print("Found at", pos+1)
else:
    print("Not Found")
'''


'''lst=[]
num=int(input("Enter the size of list: \t"))

for n in range(num):
    elements=int(input("Enter elements: \t"))
    lst.append(elements)
#print(lst)

found=False

x=int(input("Eneter a number to search: "))

for i in range(len(lst)):
    if x == lst[i]:
        found=True
        # print(f" '{x}' Element found at positon '{i+1}' " .format(x, i+1))
        print(" '{}' Element found at positon '{}' ".format(x, i + 1))
        break

if not found:
    print(" %d Elements not found in the list" %x)
'''


'''def linear_search(array, n ,x):
    for i in range(0,n):
        if array[i]==x:
            return i
    return -1

array=[2, 15, 16, 14, 9, 0]
x=int(input("Enter the finding number: "))
#x=15`
n=len(array)
result=linear_search(array, n, x)
if result==-1:
    print("Not Found")
else:
    print("Element found at:", result+1)

'''

'''pos=-1
def search(list, n):
    i=0
    pos=-1
    while i<len(list):
        if list[i] == n:
            globals()['pos']=i

            return True;
        i=i+1
    return False;


list = [5, 4, 8, 9, 2, 15]
n=15
if search(list, n):
    print("Found at=", pos+1)
else:
    print("Not Found")
'''