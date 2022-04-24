# Stack using class and object


class Stack(object):
    def __init__(self):
        self.item = []

    def push(self, item):
        self.item.append(item)
        return item

    def display(self):
        return self.item

    def pop(self):
        self.item.pop()
        return

    def peek(self):
        if self.item:
            return self.item[-1]
        else:
            return None

    def size(self):
        if self.item:
            return len(self.item)
        else:
            return None

    def is_empty(self):
        if self.item == []:
            return "Empty"
        else:
            return "Not Empty"



if __name__ == "__main__":
    st = Stack()
    st.push("1")
    st.push("2")
    print(st.display())

    print(st.size())
    print(st.peek())
    print(st.is_empty())

    st.pop()
    print(st.size())
    print(st.peek())
    print(st.is_empty())
    st.pop()
    print(st.is_empty())
    print(st.size())

    print(st.display())








'''books = []

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
'''


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