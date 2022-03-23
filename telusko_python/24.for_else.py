'''nums = [104, 13, 33, 354, 34]

for num in nums:
    if num%5==0:
        print(num)
        break
else:
    print("Not Found")
'''

for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print( n, 'equals', x, '*', n/x)
            break
    else:
        # loop fell through without finding a factor
        print(n, 'is a prime number')

