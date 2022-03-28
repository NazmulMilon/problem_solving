'''
## Required_Arguements
def add(a, b, c):
    return a+b+c
temp = add(1, 2)
print(temp)
'''


## Keyword Argument
def add(a, b, c):
    return a+b+c
temp = add(b=2, c=3, a=1)
print(temp)


#Default_Arguement
def add(a, b, c=3):
    return a+b+c
temp = add(1, 4)
print(temp)

#default arguement another example
def add(a, b, c=3):
    return a+b+c
temp = add(1, 2, 22)
print(temp)

# Variable-length argument
def add(*args):
    #print(type(args))
    tmp = 0
    for number in args:
        tmp = tmp + number
    return tmp
temp = add(1, 2, 22, 12, 17, 21, 98)
print(temp)

#examle-2
def add(**kwargs):
    print(type(kwargs))
    tmp = 0
    for key in kwargs:
        tmp = tmp + kwargs[key]
    return tmp
temp = add(a=1, b=2, c=3, d=4)
print(temp)