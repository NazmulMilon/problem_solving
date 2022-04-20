from collections import *

bank = deque(['Milon', 'Nazmul', 'Bijoy'])

print(bank)
bank.popleft()
print(bank)

# bank.popleft()
# bank.popleft()
if not bank:
    print('No person left')
