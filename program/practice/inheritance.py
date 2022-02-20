
class Phone:
    def call(self):
        print("You can call someone")

    def message(self):
        print("you can message")


class Samsung(Phone):
    def photo(self):
        print("you can take photo")


s=Samsung()
s.call()
s.message()


'''class Phone:

    def call(self):
        print("You can call someone")

    def message(self):
        print("you can message")

class Samsung:
    def call(self):
        print("You can call someone")

    def message(self):
        print("you can message")

    def photo(self):
        print("you can take photo")


s=Samsung()
s.call()
s.message()
'''