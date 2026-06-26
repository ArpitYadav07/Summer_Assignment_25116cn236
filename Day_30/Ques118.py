# Mini Library System
books = ["Python", "Java", "C++"]

while True:
    print(books)

    book = input("Issue book: ")

    if book in books:
        books.remove(book)

    print(books)

    if input("Continue? (y/n): ") == "n":
        break