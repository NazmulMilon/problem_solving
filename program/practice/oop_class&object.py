class Student:
    def __init__(self, name, roll):
        self.name=name
        self.roll=roll

    def display(self):
        print(f"Name: {self.name}, Roll: {self.roll}")


object1=Student("Milon", 3373)
object2=Student("Nazmul", 1122)


object1.display()
object2.display()

'''class Student:
    roll=""
    gpa=""

    def set_value(self, roll, gpa):
        self.roll=roll
        self.gpa=gpa

    def display(self):
        print(f"Roll: {self.roll}, GPA: {self.gpa}")


rahim=Student()
rahim.set_value(101, 204)
rahim.display()


karim=Student()
karim.roll=102
karim.gpa=4.5
karim.display()
'''