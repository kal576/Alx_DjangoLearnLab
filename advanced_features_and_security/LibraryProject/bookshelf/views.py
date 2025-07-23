from django.shortcuts import render
from django.contrib.auth.decorators import login_required, permissions_required
from .models import book
from django import forms

@login_required
@permissions_required('bookshelf.can_create', raise_exception=True)
def add_book(request):
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books}))

class SearchForm(forms.Form):
    title = forms.CharField(max_length=10)

#to prevent sql injection, use orms instead of raw sql queries
def book_search(request):
    form = SearchForm(request.GET or None)
    book = []
    if form.is_valid():
        title = form.cleaned_data['title']
        #secure orm query
        books = Book.objects.filter(title__icontains=title)
    return render(rquest, 'bookshelf/book_list.html', {'form': form, 'books': books})
