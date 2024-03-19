class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    def __str__(self):
        return f'{self.title} by {self.author}'
class PaperBook(Book):
    def __init__(self, title,autor, numPages):
        Book.__init__(self,title,autor)
        self.numPages = numPages
class EBook(Book):
    def __init__(self, title, author, size):
        Book.__init__(self,title,author)
        self.size = size

class Library:
    def __init__(self):
        self.books = []
    def addBook(self, book):
        self.books.append(book)
    def getNumBooks(self):
        return len(self.books)
myBook = Book('The Odyssey', 'Homer')
myBook2 = EBook('Lar','FP', 2)
myBook3 = PaperBook('Hum','U', 350)
print(myBook)
print(myBook2.size)
print(myBook3.numPages)
aadl = Library()
aadl.addBook(myBook)
aadl.addBook(myBook2)
aadl.addBook(myBook3)
print(aadl.getNumBooks())

