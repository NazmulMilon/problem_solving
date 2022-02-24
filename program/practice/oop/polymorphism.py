
class Bangladesh:
    def capital(self):
        print("Dhaka is the capital of BD")
    def language(self):
        print("Bangla is first language of BD")

    def type(self):
        print("BD is a poor country because of polytics")


class USA:
    def capital(self):
        print("Washington DC is the capital of USA")

    def language(self):
        print("English is the first language of USA")

    def type(self):
        print("Most development country")

obj1=Bangladesh()
obj2=USA()

for i in (obj1, obj2):
    i.capital()
    i.language()
    i.type()

#obj1.capital()
# obj1.language()
# obj1.type()

# obj2.capital()
# obj2.language()
# obj2.type()
''''
# Build in Polymorphism
print(len("Md. Milon Sarker"))
print(len([10,20,30,40,50]))


# user defined polymorphism

def add(x, y, z=0):
    return x+y+z


print(add(15,16))
print(add(12,13,14))
'''