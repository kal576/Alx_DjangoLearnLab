from django.db import models

class Author(models.Model):
    name = models.CharField()

class Book(models.Model):
    title = models.CharField()
    author = models.ForeignKey('Author', on_delete=models.CASCADE)

class Library(models.Model):
    name = models.CharField()
    books = models.ManyToManyField(Book)

class Librarian(models.Model):
    name = models.CharField()
    library = models.OneToOneField(Library)


