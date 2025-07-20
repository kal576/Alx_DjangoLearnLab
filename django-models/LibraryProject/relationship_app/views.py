from django.shortcuts import render, redirect
from django.views.generic.detail import DetailView
from .models import Book
from .models import Library
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.decorators import permission_required
from .forms import BookForm

#add permissions
@permission_required('relationship_app.can_add_book')
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_books')
    else:
        form = BookForm()
    return render(request, 'relationship_app/book_form.html', {'form': form, 'action': 'Add'})

# View to edit a book
@permission_required('relationship_app.can_change_book')
def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('list_books')
    else:
        form = BookForm(instance=book)
    return render(request, 'relationship_app/book_form.html', {'form': form, 'action': 'Edit'})

# View to delete a book
@permission_required('relationship_app.can_delete_book')
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('list_books')
    return render(request, 'relationship_app/book_confirm_delete.html', {'book': book})

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

#role based access
def is_admin(user):
    return user.is_authenticated adn user.userprofile.role == 'Admin'

def is_librarian(user):
    return user.is_authenticated adn user.userprofile.role == 'Librarian'

def is_member(user):
    return user.is_authenticated adn user.userprofile.role == 'Member'

@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html', {'message': 'Welcome, Admin!'})

@user_passes_test(is_admin)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html', {'message': 'Welcome, Librarian!'})

@user_passes_test(is_admin)
def member_view(request):
    return render(request, 'relationship_app/member_view.html', {'message': 'Welcome, Member!'})

#enforcing permissions
def
