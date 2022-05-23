

class Person:
    def __init__(self, person_name, date_of_birth, ht):
        self.name = person_name
        self.date_of_birth = date_of_birth
        self.height = ht

    def get_name(self):
        return self.name

    def set_name(self, new_name):
        if self.__has_any_number(new_name):
            print("Sorry person name can't have number")
            return
        self.name = new_name

    def __has_any_number(self, string):
        return "0" in string

    def get_summary(self):
        return f"Name: {self.name}, DOB: {self.date_of_birth}, Height: {self.height}"


a_person = Person("Milon", "1996", "%.5 feet")
print(a_person.get_summary())
a_person.set_name("Nazmul Milon")
print(a_person.get_summary())

print(a_person.date_of_birth) #this case there will no bracket (). because
                                #bracket indicate that it's a function.
a_person.set_name("0Nazmul")
print(a_person.name)