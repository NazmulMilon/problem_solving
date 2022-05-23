

class Person:
    def __init__(self, person_name, date_of_birth, ht):
        self.name = person_name
        self.date_of_birth = date_of_birth
        self.height = ht

    def get_name(self):
        return self.name

    def get_summary(self):
        return f"Name: {self.name}, DOB: {self.date_of_birth}, Height: {self.height}"


a_person = Person("Milon", "1996", "%.5 feet")
print(a_person.get_summary())