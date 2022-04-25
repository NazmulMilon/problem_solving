from collections import deque


class Queue:
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
