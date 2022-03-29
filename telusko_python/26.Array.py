from array import *

vals = array('i', [4, 5, 2, 7, 7, 8])
newArray = array(vals.typecode, (a*a for a in vals))

i=0
while i<len(newArray):
    print(newArray[i], end=' ')
    i+=1

'''vals.reverse()
# print(vals)
# print(vals.buffer_info())
print(vals)
print(vals[1])
'''

'''for e in vals:
    print(e, end=' ')'''

'''for i in range(len(vals)):
    print(vals[i], end=' ')'''


'''for i in range(5):
    print(vals[i], end=' ')
    '''

'''
vals = array('i', [4, 5, 2, 7, 7, 8])
newArray = array(vals.typecode, (a*a for a in vals))
for e in newArray:
    print(e, end=' ')
'''
