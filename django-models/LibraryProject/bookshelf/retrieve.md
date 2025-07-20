#retrieve operation

from bookshelf.models import Book

books = Book.objects.get(titel="1984")

#expected output: 1984 by George Orwell
