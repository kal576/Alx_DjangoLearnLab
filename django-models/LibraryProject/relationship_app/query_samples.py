from .models.py import Books, Library, Librarian

#querying all books by a specific author
def books_by_author(author_name):
    author = Author.objects.get(name=author_name)
    books = Books.objects.filter(author=author)
    for book in books:
        print(f"{book.title}")

#listing all books in a library
def listing_books(library_name):
    library = Library.objects.get(name=library_name)
    books = library.books.all()
    for book in books:
        print(f"{book.title}")

#retrieving librarian for a library
def librarians(librarian_name):
    library = Librarian.objects.get(name=librarian_name)
    librarian = Librarian.objects.get(library=library)
    print(f"{name} is the librarian for {libray}")
