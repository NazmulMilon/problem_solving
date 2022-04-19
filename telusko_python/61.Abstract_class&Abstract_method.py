from abc import ABC, abstractmethod

'''
# abstract class
class Computer(ABC):
    @abstractmethod
    def process(self):
        pass


class Laptop(Computer):
    def process(self):
        print("It's Running")


# com = Computer(
# com.process()
com1 = Laptop()
com1.process()

'''


class Computer(ABC):
    @abstractmethod
    def process(self):
        pass


class Laptop(Computer):
    def process(self):
        print("It's Running")


class Programmer:
    def work(self, com):
        print("Solving Bugs")
        com.process()


# com = Computer(
# com.process()
com1 = Laptop()

prog1 = Programmer()
prog1.work(com1)
# com1.process()
