from collections import deque

class Queue(object):
    def __init__(self):
        self.item = []

    def enqueue(self, item):
        self.item.insert(0, item)

    def dequeue(self):
        if self.item:
            self.item.pop()
        else:
            return None

    def peek(self):
        if self.item:
            return self.item[-1]

    def display(self):
        return self.item

    def is_empty(self):
        if self.item==[]:
            return True
        else:
            return False

    def size(self):
        return len(self.item)


if __name__ == "__main__":
    qu = Queue()
    qu.enqueue(item=1)
    qu.enqueue(item=2)
    qu.enqueue(item=5)
    print(qu.display())
    print("Size\t{}".format(qu.size()))
    print("Peek\t{}".format(qu.peek()))


    qu.dequeue()
    print("Size\t{}".format(qu.size()))
    print(qu.display())

    print("Peek\t{}".format(qu.peek()))
    print(qu.display())





'''class Queue:
    def __init__(self):
        self.buffer = deque()

    def enqueue(self, val):
        self.buffer.appendleft(val)

    def dequeuee(self):
        return self.buffer.pop()

    def is_empty(self):
        return len(self.buffer) ==0

    def size(self):
        return len(self.buffer)


object = Queue()
object.enqueue(val)
object.dequeuee()
object.is_empty()
object.size(
'''

'''bank = deque(['Nazmul', 'Hasan', 'Milon', 'Ahmed'])
print(bank)

bank.popleft()
print(bank)

bank.popleft()
bank.popleft()
bank.popleft()

if not bank:
    print("No person left")
'''

'''
from collections import *

bank = deque(['Milon', 'Nazmul', 'Bijoy'])

print(bank)
bank.popleft()
print(bank)

# bank.popleft()
# bank.popleft()
if not bank:
    print('No person left')
'''
