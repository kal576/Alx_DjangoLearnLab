from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

class CustomUserManager(BaseUserManager):
    def CreateUser(self, username, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Email is a required field')
        if not username:
            raise ValueError('Username is a required field')

        email = self.normalize_email(email) #ensures email is in lower case
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password) #hashes password
        user.save(using=self._db)
        return user

    def SuperUser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('The user is not a superuser')
        if extra_fields.get('is_staff') is not True:
            raise ValueError('The user is not a staff')

        return self.create_user(username, email, password, **extra_fields)

class CustomUser(AbstractUser):
    date_of_birth = models.DateField(null=True, blank=True)
    profile_photo = models.ImageField(upload_to='profile_photos/', null=True, blank=True)

class Book(models.Model):
    title: models.CharField(max_length=200)
    author: models.CharField(max_length=100)
    publication_year: models.IntegerField()

    class Meta:
        permissions = [
                ("can_view", "Can view book"),
                ("can_create", "Can create book"),
                ("can_edit", "Can edit book"),
                ("can_delete", "Can delete book"),
            ]

    def __str__(self):
        return f"{self.title} by {self.author}"
