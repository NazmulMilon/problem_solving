my_list = [2, 3, 4, 5, 6, 7]

def square(x):
    return x * x
new_list = map(square, my_list)
print(new_list)
print(list(new_list))