
from threading import *
from time import sleep

class Hello(Thread):
    def run(self):
        for i in range(5):
            print("Hello")
            sleep(0.5)

class Hi(Thread):
    def run(self):
        for i in range(5):
            print("Hi")
            sleep(0.5)

t1 = Hello()
t2 = Hi()

t1.start()
sleep(0.2)
t2.start()

t1.join()
t2.join()
print("Bye")


'''class Hello(Thread):
    def run(self):
        for i in range(5):
            print("Hello")
            sleep(1)


class Hi(Thread):
    def run(self):
        for i in range(5):
            print("Hi")
            sleep(1)


t1 = Hello()
t2 = Hi()

# t1.run() #its not possible because run() method is a build in method of thread

t1.start()
sleep(0.2)
t2.start()

t1.join()
t2.join()

print("Bye")
'''

'''
class Hello(Thread):
    def run(self):
        for i in range(5):
            print("Hello")
            sleep(1)


class Hi(Thread):
    def run(self):
        for i in range(5):
            print("Hi")
            sleep(1)


t1 = Hello()
t2 = Hi()

# t1.run() #its not possible because run() method is a build in method of thread

t1.start()
sleep(0.2)
t2.start()
'''