#factorial_number
print('Please input your number:')
number = int(input())
temp = number

while number > 1:
    number -= 1
    temp = temp*number

if temp == 0:
    print(1)
else:
    print(temp)

#factorial example
def factorial(number):
    if number == 0:
        return 1
    else:
        return number * factorial(number - 1)

print('Please input your number:')
number = int(input())
print(factorial(number))