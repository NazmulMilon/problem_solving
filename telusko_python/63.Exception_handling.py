

# another Way to handle exception
a=5
b=0

try:
    print(a/b)
except Exception as e:
    print("Hey, You can't divide a number by 0. ", e)

print("Bye")


'''a=5
b=0

try:
    print(a/b)

except Exception:
    print("Hey, You can't divide a number by 0")
print("Bye")
'''
