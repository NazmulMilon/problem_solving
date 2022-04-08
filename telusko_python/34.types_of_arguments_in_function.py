#variable length argument

def add(*b):
    c=0
    for i in b:
        c=i+c
    print(c)

add(4, 5, 6, 7)

'''
# variable length argument
def add(a, *b):
    c=a
    for i in b:
        c=c+i
    print(c)

add(5, 6, 7, 2)
'''



''' 
# default argument
def person(name, age=15):
    print(name, age)


person('nazmul')
#person('nazmul', 25)
'''
'''
# keyword arguments
def person(name, age):
    print(name, age)
    
person(name='milon', age=19)
'''


'''
# position arguments
def person(name, age):

    print(name, age)


person('milon', 28)
'''