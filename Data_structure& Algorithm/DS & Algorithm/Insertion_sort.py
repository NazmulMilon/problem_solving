
# FelixTechTips (youtube channel)


def insertion_sort(arr):
    for i in range(1, len(arr)):
        j=i
        while arr[j-1]>arr[j] and j>0:
            arr[j-1], arr[j] = arr[j], arr[j-1]
            j-=1


tests = [
    [23, 2, 1, 76, 8, 19, 90, 80],
    [90, 23, 0, 15, 9],
    [88, 15, 31, 29, 11, 5],
    [1],
    [0]
]

arr = [23, 2, 1, 76, 8, 19, 90, 80]

for kk in tests:
    insertion_sort(kk)
    print(kk)


insertion_sort(arr)
print(arr)



'''#code_basics

def insertion_sort(arr):
    for i in range(1, len(elements)):
        anchor = elements[i]
        j=i-1
        while j>=0 and anchor<elements[j]:
            elements[j+1] = elements[j]
            j=j-1
        elements[j+1] = anchor


elements = [11, 9, 29, 7, 2, 15, 28]

insertion_sort(elements)
print(elements)
'''

'''
# FelixTechTips (youtube channel)
def insertion_sort(arr):
    for i in range(1, len(arr)):
        j=i
        while arr[j-1]>arr[j] and j>0:
            arr[j-1], arr[j] = arr[j], arr[j-1]
            j-=1


arr = [23, 2, 1, 76, 8, 19, 90, 80]

insertion_sort(arr)
print(arr)
'''

'''def insertion_sort(arr):
    for i in range(1, len(arr)):
        j = i
        while arr[j-1]>arr[j] and j>0:
            arr[j-1], arr[j] = arr[j], arr[j-1]
            j=j-1


arr =[2, 6, 5, 1, 3, 4]

insertion_sort(arr)
print(arr)'''