from .models.py import Books, Library, Librarian

#querying all books by a specific author
def books_by_author(author_name):
    books = Books.objects.filter(author__name=author_name)
    for book in books:
        print(f"{book.title}")

#listing all books in a library
def listing_books(library_name):
    library = Library.objects.get(name=library_name)
    books = ibrary.objects.all()
    for book in books:
        print(f"{book.title}")

#retrieving librarian for a library
def librarians(librarian_name):
    librarian = Librarian.objects.get(librarian_name=name)
    print(f"{name} is the librarian for {libray}")
