
# bubble sort in efficient way

def bubble_sort(lst):
    for i in range(len(lst)-1):
        swapped = False
        for j in range(len(lst)-1-i):
            if lst[j]>lst[j+1]:
                temp = lst[j]
                lst[j]=lst[j+1]
                lst[j+1]=temp
                swapped = True
        if not swapped:
            break


lst = list(map(int,input("Enter the number of elements: ").split()))

bubble_sort(lst)
print(lst)



'''
# bubble sort in different way
def bubble_sort(lst):
    arr = len(lst)
    for i in range(arr-1):
        for j in range(arr-1-i):
            if lst[j]>lst[j+1]:
                temp = lst[j]
                lst[j]=lst[j+1]
                lst[j+1]=temp


lst = list(map(int,input("Enter numbers: ").split()))

bubble_sort(lst)
print(lst)
'''

'''
# bubble sort in another way
def bubble_sort(arr):
    for i in range(len(arr)-1):
        for j in range(len(arr)-1-i):
            if arr[j]>arr[j+1]:
                temp=arr[j]
                arr[j]=arr[j+1]
                arr[j+1]=temp


arr = list(map(int,input("Enter elements:").split()))


bubble_sort(arr)
print(arr)
'''

'''
# bubble sort in simple way
def bubble_sort(lst):

    for i in range(len(lst)):
        for j in range(len(lst)-1-i):
            if lst[j]>lst[j+1]:
                temp = lst[j]
                lst[j]=lst[j+1]
                lst[j+1]=temp


lst = [4, 10, 25, 95, 14, 9, 59, 7]


res=bubble_sort(lst)
print(lst)
'''
