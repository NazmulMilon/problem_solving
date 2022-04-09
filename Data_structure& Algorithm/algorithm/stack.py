

book = []
book.append("Learn C")
book.append("Learn C++")
book.append("Learn Java")

print(book)

print(book.pop())
print("Last Item of book is: ", book[-1])

print(book.pop())
print("Last Item of book is: ", book[-1])

print(book.pop())
if not book:
    print("Books  not found in list.")


'''book.insert(1, 'Python')
print(book)'''