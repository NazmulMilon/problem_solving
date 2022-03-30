class Dog:
    # class attribute
    attr1="mamma1"

    # instance attribute
    def __init__(self, name):
        self.name=name

    def speak(self):
        print(f"My name is: {self.name}")


# object instiation
Rodger=Dog('AGGGG')
Tommy=Dog('BFFFFF')

Rodger.speak()
Tommy.speak()