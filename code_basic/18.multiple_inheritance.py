class Father:
    def skills(self):
        print("I love gardening")

class Mother:
    def skills(self):
        print("I love cooking")

class Child(Father, Mother):
    def skills(self):
        Father.skills(self)
        Mother.skills(self)
        print("I love sports")

c = Child()
c.skills()
'''
class Father:
    def gardening(self):
        print("I love gardening")

class Mother:
    def cooking(self):
        print("I love cooking")

class Child(Father, Mother):
    def sports(self):
        print("I love sports")

c = Child()
c.gardening()
c.cooking()
c.sports()
'''