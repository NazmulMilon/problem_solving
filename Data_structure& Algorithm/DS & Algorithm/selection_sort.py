lst = list(map(int, input("Enter the numbers: ").split()))

def selection_sort(lst):
    for i in range(len(lst)):
        minpos=i
        for j in range(i, len(lst)):
            if lst[j]<lst[minpos]:
                minpos=j

        lst[i], lst[minpos] = lst[minpos], lst[i]


selection_sort(lst)
print(lst)


'''
lst = [10, 34, 24, 92, 4, 103]

def selection_sort(lst):
    for i in range(len(lst)):
        min=i
        for j in range(i, len(lst)):
            # min=i
            if lst[j]<lst[min]:
                min=j

        temp = lst[i]
        lst[i] = lst[min]
        lst[min] = temp

selection_sort(lst)
print(lst)
'''


'''
lst = [9, 3, 12, 54, 22, 55]

def selection_sort(lst):

    for i in range(len(lst)):
        minpos = i
        for j in range(i,len(lst)):
            if lst[j]<lst[minpos]:
                minpos=j

        temp = lst[i]
        lst[i] = lst[minpos]
        lst[minpos] = temp


selection_sort(lst)
print(lst)
'''


'''def sort(nums):
    for i in range(5):
        minpos=i
        for j in range(i,6):
            if nums[j]<nums[minpos]:
                minpos=j
        temp=nums[i]
        nums[i]=nums[minpos]
        nums[minpos]=temp



nums=[5,6,3,9,2,33]
sort(nums)
print(nums)'''