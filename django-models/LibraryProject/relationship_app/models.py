from django.db import models

class Author(models.Model):
    name = models.CharField()
    
    def __str__(self):
        return self.name    

class Book(models.Model):
    title = models.CharField()
    author = models.ForeignKey('Author', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Library(models.Model):
    name = models.CharField()
    books = models.ManyToManyField(Book)

    def __str__(self):
        return self.name

class Librarian(models.Model):
    name = models.CharField()
    library = models.OneToOneField(Library)

    def __str__(self):
        return self.name


