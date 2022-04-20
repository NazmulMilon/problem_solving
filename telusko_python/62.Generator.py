
def topten():
    n=1
    while n<=10:
        sq = n*n
        yield sq
        n+=1


values = topten()

for i in values:
    print(i)


'''
def topten():
    yield 1
    yield 2
    yield 3
    yield 4


values = topten()

print(values.__next__())
print(values.__next__())


for i in values:
    print(i)
'''


'''
def topten():
    yield 1
    yield 2
    yield 3
    yield 4


values = topten()

print(values.__next__())
print(values.__next__())
print(values.__next__())
'''

'''
def topten():
    
    yield 5


values = topten()
print(values.__next__())
'''