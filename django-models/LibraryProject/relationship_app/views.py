from django.shortcuts import render, redirect
from django.views.generic.detail import DetailView
from .models import Book
from .models import Library
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

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

#user registration
def register_user(request):
    if request.method='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('list_books')
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})
