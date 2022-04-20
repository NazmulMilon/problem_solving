
lst = [22, 45, 7, 9, 10, 99]

it = iter(lst)
print(it.__next__())
print(it.__next__())
print(it.__next__())

print(next(it)) # another way of calling the next value

for i in lst:
    print(i)
    # print(i, end=" ")