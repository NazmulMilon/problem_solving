from numpy import *

m1 = matrix('2 3 4; 5 6 5; 7 8 9 ')
m2 = matrix('1 2 3; 6 8 5; 2 6 7 ')

m3 = m1 * m2
print(m3)

'''
m = matrix('2 3 4; 5 6 5; 7 8 0 ')
#m = matrix('2 3; 4 5; 6 5; 7 8')


print(diagonal(m))
print(m.min())
print(m.max())
'''

'''
arr1 = array([

    [2, 3, 4, 5],
    [7, 8, 9, 0],
])

# m=matrix(arr1)
# m = matrix('2, 3, 4, 5; 7, 8, 9, 0')
m = matrix('2 3 4 5; 7 8 9 0')

print(m)
'''

'''
arr1 = array([

    [2, 3, 4, 5, 6, 2],
    [7, 8, 9, 0, 1, 3],
])

arr2 = arr1.flatten()
# arr3 = arr1.reshape(3, 4) # reshape the matrix
arr3 = arr1.reshape(2,2,3)

print(arr3)
'''

'''
arr1 = array([

    [2, 3, 4, 5, 6, 2],
    [7, 8, 9, 0, 1, 3],
])

arr2 = arr1.flatten()
print(arr2)
'''


'''
arr1 = array([

    [2, 3, 4, 5, 6],
    [7, 8, 9, 0, 1],
])

#print(arr1)
# print(arr1.dtype)
#print(arr1.ndim)
print(arr1.shape)
print(arr1.size)
'''