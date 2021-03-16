class Book:
    def __init__(self, content: str):
        self.content = content


class Formatter:
    def format(self, book: Book) -> str:
        return book.content


class TrimContentFormatter:
    def format(self, book: Book) -> str:
        return book.content[:3]


class Printer:
    def get_book(self, book: Book, formatter):
        return formatter.format(book)


book = Book('Goblet of fire')
print(Printer().get_book(book, Formatter()))
print(Printer().get_book(book, TrimContentFormatter()))

'''
We want to be able to print books, but before printing the book we should be able to format it. 
To accomplish this we have a class that can print books called Printer and a class Formatter which is used by Printer. 
Refactor the provided code that breaks the DIP because both Printer and Formatter 
depend on concretions, not abstractions by creating some abstractions and inject them wherever they are needed.
'''