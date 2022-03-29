class Computer:
    def __init__(self, cpu, ram):
        self.cpu=cpu
        self.ram=ram

    def config(self):
        print("Config is: ", self.cpu, self.ram)


com1=Computer('i5', 4)
com2=Computer('i3', 8)

com1.config()
com2.config()

'''class Computer:
    def __init__(self):
        print("Init method called automatically")

    def config(self):
        print("Config is: ")


com1 = Computer()
com2 = Computer()

com1.config()
com2.config()
'''