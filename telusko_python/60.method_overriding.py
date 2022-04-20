
class Phone:
    def display(self):
        print("I am in phone class")


class Samsung(Phone):
    # pass           # if no method call only pass it will print the value of Phone class
    def display(self):
        super().display()
        print("I am in Samsung Class")


s1 = Samsung()
s1.display()



'''class A:

    def show(self):
        print("in A Show")


class B(A):
    def show(self):
        print("in B Show")


a1 = B()
a1.show()'''