class University:
    def __init__(self, name, position):
        self.name=name
        self.position=position

    def display(self):
        print(f"University Name: {self.name}, Position: {self.position}")


object1 = University('IUBAT', '5th')
object2 = University('BUET', '2nd')

object1.display()
object2.display()
