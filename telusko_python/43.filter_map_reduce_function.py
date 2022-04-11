
#map function
def update(n):
    return n*2


nums = [2, 3, 5, 4, 6]

double = list(map(update, nums))

print(double)


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