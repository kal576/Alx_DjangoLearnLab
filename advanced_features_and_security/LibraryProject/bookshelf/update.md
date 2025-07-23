#insert operation

from bookshelf.models import Book

book=Book.objects.get(title=1984)
book.title = "Nineteen Eighty-Four"
book.save()

#expected output: Nineteen Eighty-Four by George Orwell
