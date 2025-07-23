from django.shortcuts import render
from django.contrib.auth.decorators import login_required, permissions_required

@login_required
@permissions_required('bookshelf.can_create', raise_exception=True)
def add_book(request):
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books}))

