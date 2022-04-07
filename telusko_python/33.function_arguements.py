
def update(lst):

    print(id(lst))
    lst[1]=25
    print(id(lst))
    print('x is:', lst)


lst=[10, 20, 30]
print(id(lst))
update(lst)
print('lst is: ', lst)


'''def update(x):

    print(id(x))
    x=8
    print(id(x))
    print('x is:', x)


a=10
print(id(a))
update(a)
print('a is: ', a)
'''