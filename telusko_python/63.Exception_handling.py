# another Way to handle exception using specific exceptions name
a=5
b=2

try:
    print("resource open")
    print(a/b)
    k = int(input("Enter a number: "))
    print(k)

except ZeroDivisionError as e:
    print("Hey, You can't divide a number by 0. ", e)

except ValueError as e:
    print("Invalid Input")

except Exception as e:
    print("Something went wrong")

finally:
    print("resource closed.")


'''# another Way to handle exception using finally
a=5
b=2

try:
    print("resource open")
    print(a/b)

except Exception as e:
    print("Hey, You can't divide a number by 0. ", e)

finally:
    print("resource closed.")
'''

'''
# another Way to handle exception
a=5
b=0

try:
    print(a/b)
except Exception as e:
    print("Hey, You can't divide a number by 0. ", e)

print("Bye")
'''

'''a=5
b=0

try:
    print(a/b)

except Exception:
    print("Hey, You can't divide a number by 0")
print("Bye")
'''
