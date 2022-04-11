from functools import reduce

nums = [3, 4, 6, 8, 4, 6, 2, 9]

evens = list(filter(lambda n: n%2==0, nums))

doubles = list(map(lambda n: n*2, evens))
print(doubles)

sum = reduce(lambda a,b : a+b, doubles)
print(sum)


'''
# reduce function using lambda
nums = [2, 4, 8, 25, 13, 48]

sum = reduce(lambda a,b : a+b, nums)
print(nums)
print(sum)
'''

'''# reduce function
def add_all(a, b):
    return a+b

nums = [2, 4, 8, 25, 13, 98]

sum = reduce(add_all, nums)

print(nums)
print(sum)
'''


'''# map function using lambda

nums = [22, 4, 5, 7, 8, 6]

double = list(map(lambda n: n*2, nums))
print(double)'''

'''#map function
def update(n):
    return n*2


nums = [2, 3, 5, 4, 6]

double = list(map(update, nums))

print(double)
'''



'''# filter function using lambda function
nums = [12, 34, 11, 14, 65, 78]

evens = list(filter(lambda n:n%2==0, nums))
print(evens)
'''


# filter function
'''def is_even(n):
    return n%2==0


nums = [3, 2, 6, 8, 14, 16, 22, 9]

evens = list(filter(is_even, nums))

print(evens)'''