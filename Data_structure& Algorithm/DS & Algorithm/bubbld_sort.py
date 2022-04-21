

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
