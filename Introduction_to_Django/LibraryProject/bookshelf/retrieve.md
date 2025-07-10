#retrieve operation

from bookshelf.models import Book

books = Book.objects.all()

#expected output: 1984 by George Orwell
