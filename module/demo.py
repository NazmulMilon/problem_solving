import module2
'''from 45.module import *
a = 7
b = 5

c = add(a, b)
print(c)'''

'''import 45.module

a = 7
b = 6

c = 45.module.add(a, b)
print(c)'''


from module import *

a = 10
b = 8

c1 = add(a, b)
print(c1)

c2 = sub(a, b)
print(c2)

c3 = mul(a, b)
print(c3)

c4 = div(a, b)
print(c4)



a = 100
b = 8

d = module2.mul(a, b)
print(d)