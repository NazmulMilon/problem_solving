# method overriding with constructor method

class Phone:
    def __init__(self):
        print("I am in Phone Class")


class Samsung(Phone):
    def __init__(self):
        super().__init__()
        print("I am in Samsung Class")

s1=Samsung()


'''
# method overriding with method
class Phone:
    def display(self):
        print("I am in phone class")


class Samsung(Phone):
    # pass           # if no method call only pass it will print the value of Phone class
    def display(self):
        super().display()
        print("I am in Samsung Class")


s1 = Samsung()
#s1.display()
'''


'''class A:

    def show(self):
        print("in A Show")


class B(A):
    def show(self):
        print("in B Show")


a1 = B()
a1.show()'''