class Dog:

    # class variable
    animal = 'monkey'

    # constructor or init method
    def __init__(self, color, age, breed):

        # instance variable
        self.color = color
        self.age=age
        self.breed=breed

    def display(self):
        print(f"Color: {self.color}, Age: {self.age}, Breed: {self.age}")


object1=Dog('White', 22, 4)
object2=Dog('black', 17, 5)

print(object1.animal)
object1.display()

print(object2.animal)
object2.display()

# class variable can access using class
print("\nAccessing class variable using class name")
print(Dog.animal)