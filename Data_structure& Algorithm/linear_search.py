def linear_search(array, n ,x):
    for i in range(0,n):
        if array[i]==x:
            return i
    return -1


array=[2, 15, 16, 14, 9, 0]
x=int(input("Enter the finding number: "))
#x=15
n=len(array)
result=linear_search(array, n, x)
if result==-1:
    print("Not Found")
else:
    print("Element found at:", result+1)
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