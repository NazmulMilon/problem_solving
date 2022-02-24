class BD():
    def capital(self):
        print("Dhaka  is the capital of BD.")

    def language(self):
        print("Bangla is the most widely spoken language of BD.")

    def type(self):
        print("Bangladesh is a developing country.")


class USA():
    def capital(self):
        print("Washington, D.C. is the capital of USA.")

    def language(self):
        print("English is the primary language of USA.")

    def type(self):
        print("USA is a developed country.")


def func(obj):
    obj.capital()
    obj.language()
    obj.type()

obj_bd=BD()
obj_usa=USA()


func(obj_bd)
func(obj_usa)