from numpy import *


arr = ones(5)
print(arr)

'''arr = zeros(5)
print(arr)
'''

'''
# using logspace
# arr= logspace(1, 40, 5)
# print(arr)
arr = logspace(1, 40, 5)
print('%.2f' %arr[2])
'''

'''
# using arange
# arr= arange(1, 20, 3)
arr=arange(1, 20, 2)
print(arr)
'''

'''
#using linspace
#arr = linspace(1, 10, 15)
#arr=linspace(1, 20, 22)
#arr = linspace(1, 20, 5)
#arr=linspace(0, 15, 16)
arr=linspace(1, 15) #it will make default 50 value

print(arr)
'''

'''
# using array() 
arr = array([1, 3, 4 ,6,7, 9], float)
arr = array([1, 3, 4 ,6,7, 9], int)

print(arr.dtype)
print(arr)
'''
