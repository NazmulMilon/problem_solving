
# keyword variable length arguments

def person(name, **data):
    print(name)

    for i, j in data.items():
        print(i, j)


person('navin', age=18, city='dhaka', mob=777783667)

'''
# keyword variable length arguments
def person(name, **data):
    print(name)
    print(data)


person('navin', age=18, city='dhaka', mob=777783667)
'''

'''
def person(name, *data):
    print(name)
    print(data)


person('navin', 18, 'dhaka', 83667)
#person(navin, age=18, dhaka, mob=0183667)
'''
