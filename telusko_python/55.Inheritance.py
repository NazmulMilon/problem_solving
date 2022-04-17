
'''
# Single Inheritance
class A:
    def feature1(self):
        print("Feature 1 Working")

    def feature2(self):
        print("Feature 2 working")


class B(A):
    def feature3(self):
        print("Feature 3 Working")

    def feature4(self):
        print("Feature 4 Working")


b1 = B()
b1.feature1()
b1.feature2()
b1.feature3()
b1.feature4()
'''

'''
# Multilevel Inheritance
class A:
    def feature1(self):
        print("Feature 1 Working")

    def feature2(self):
        print("Feature 2 working")


class B(A):
    def feature3(self):
        print("Feature 3 Working")

    def feature4(self):
        print("Feature 4 Working")


class C(B):
    def feature5(self):
        print("Feature 5 Working")


c1 = C()
c1.feature1()
c1.feature2()
c1.feature3()
c1.feature4()
c1.feature5()'''


# Multiple Inheritance
class A:
    def feature1(self):
        print("Feature 1 Working")

    def feature2(self):
        print("Feature 2 working")


class B:
    def feature3(self):
        print("Feature 3 Working")

    def feature4(self):
        print("Feature 4 Working")


class C(A, B):
    def feature5(self):
        print("Feature 5 Working")


b1 = B()
b1.feature3() # We can not access other features.
b1.feature4()

c1 = C()
c1.feature1()
c1.feature2()
c1.feature3()
c1.feature4()
c1.feature5()