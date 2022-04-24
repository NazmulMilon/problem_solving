books = []

books.append("Learn C")
books.append("Learn C++")
books.append("Learn Java")
books.append("Python")
print(books)

books.pop()
print(books)

books.pop()
print("New books is: ", books[-1])

books.pop()
print(books)

books.pop()
if not books:
    print("No books left")

'''book = []
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
'''

'''book.insert(1, 'Python')
print(book)'''