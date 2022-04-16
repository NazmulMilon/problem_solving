

class Car:
    wheels = 4

    def __init__(self):
        self.mil = 10
        self.com = 'BMW'


c1 = Car()
c2 = Car()

c1.mil = 8 # if we want to change the instance variable.

Car.wheels = 5 # if we want to change the class variable.

print(c1.com, c1.mil, c1.wheels)
print(c2.com, c2.mil, c2.wheels)