'''
number = int(input("Enter a number: "))
reverse=0
while number!=0:
    digit=number%10
    reverse=reverse*10+digit
    number=number//10
print(reverse)
'''

def reverse(number):
    re=0
    while number!=0:
        digit=number%10
        re=re*10+digit
        number=number//10
    return re
number=int(input("Enter a number: "))
print(reverse(number))