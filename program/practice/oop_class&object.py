class Student:
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