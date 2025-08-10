from django.db import models

class Author(models.Model):
    """Author model"""
    name = models.CharField(max_length=255)
    
class Book(models.Model):
    """Book model"""
    title = models.CharField(max_length=255)
    publication_year = models.IntegerField()
    author = models.ForeignKey(
            Author, on_delete=models.CASCADE)
