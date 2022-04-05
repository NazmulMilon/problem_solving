from numpy import *

# Shallow copy
arr1 = array([2, 3, 4, 6])
arr2 = arr1.view()

arr1[1] =15
print(arr1)
print(arr2)

print(id(arr1))
print(id(arr2))

'''arr1 = array([5, 3, 6, 9, 4])
arr2 = array([9, 2, 4, 6, 9])
print(concatenate([arr1, arr2]))
'''


'''
arr = array([5, 3, 6, 5, 6,  9, 4, 8, 9])

# print(sin(arr))
# print(cos(arr))
# print(sqrt(arr))
# print(sum(arr))
# print(max(arr))
# print(min(arr))
# print(sort(arr))
print(unique(arr))
'''



'''
# vectorized operation/ add two array
arr1 = array([5, 3, 6, 9, 4])
arr2 = array([9, 2, 4, 6, 9])
arr3 = arr1 + arr2
print(arr3)
'''

'''# add 5 to each elements
arr = array([2, 4, 5 ,6, 7])
arr = arr+5
print(arr)
'''