from django.shortcuts import render
from django.views.generic import DetailView
from .models import Book
from .models import Library

# Function-based view to display all books
def list_books(request):
    books = Book.objects.all()  # Get all books from the database
    return render(request, 'relationship_app/list_books.html', {'books': books})  # Render template with books

# Class-based view to display details of a specific library
class LibraryDetailView(DetailView):
    model = Library  # Model for the view
    template_name = 'relationship_app/library_detail.html'  # Template for rendering
    context_object_name = 'library'  # Name used in template for library object

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = self.object.books.all()  # Add all books in the library

