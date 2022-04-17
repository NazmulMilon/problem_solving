class A:
    def __init__(self):
        print("in A Init")

    def feature1(self):
        print("Feature 1 Working")

    def feature2(self):
        print("Feature 2 working")


class B(A):
    def __init__(self):
        super().__init__() # to call init method of class A, we need super() method
        print("in B Init")
        '''if you create object of subclass it will first try find
        init of subclass. If it is not found then it will call init of super class.'''

    def feature3(self):
        print("Feature 3 Working")

    def feature4(self):
        print("Feature 4 Working")


# a1 = A()

b1 = B()