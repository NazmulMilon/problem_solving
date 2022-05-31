"""Implement quick sort in Python.
Input a list.
Output a sorted list."""
def swap(a, b, arr):
    if a != b:
        temp = arr[a]
        arr[a] = arr[b]
        arr[b] = temp


def partition(test, start, end):
    pivot_index = start
    pivot = test[pivot_index]

    while start < end:

        while start < len(test) and test[start] <= pivot:
            start += 1

        while test[end] > pivot:
            end -= 1

        if start < end:
            swap(start, end, test)

    swap(pivot_index, end, test)

    return end


def quicksort(test, start, end):
    if start < end:
        pi = partition(test, start, end)
        quicksort(test, start, pi - 1) # left partition
        quicksort(test, pi + 1, end)   #right partition


test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
quicksort(test, 0, len(test)-1)
print(test)