
a = 15
print(id(a))


def local_variable():
    a=20
    x = globals()['a']
    print(id(x))

    print('local:', a)

    globals()['a'] = 25


local_variable()


print('Global:',a)


'''
a = 15


def local_variable():
    global a
    a=20
    print('local:', a)


local_variable()


print('Global:',a)
'''