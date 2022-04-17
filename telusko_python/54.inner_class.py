
class Student:
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll
        self.lap = self.Laptop() #inner class objects

    def show(self):
        print(self.name, self.roll)
        self.lap.show() #inner class show

    class Laptop:

        def __init__(self):
            self.brand = 'HP'
            self.cpu = 'i5'
            self.ram = 8

        def show(self):
            print(self.brand, self.cpu, self.ram)


s1 = Student('Milon', 5)
s2 = Student('Nazmul', 2)

s1.show()
