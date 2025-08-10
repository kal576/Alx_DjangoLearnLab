#delete operation

from bookshelf.models import Book
book = Book.objects.all(title="Nineteen Eighty-Four")
book.delete()

#try retrieving
try:
    Book.objects.get(id=1)
except Book.DoesNotExist:
    print("Book does not exist")

#expected output: Book does not exist
