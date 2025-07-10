from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdin):
    list_display = ('title', 'author', 'publication_year')

admin.site.register(Book, BookAdmin)
