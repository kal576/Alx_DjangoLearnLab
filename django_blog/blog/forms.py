from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Comment
from .models import Post

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class PostForm(forms.ModelForm):
    tags = forms.CharField(
        required=False,
    )

    class Meta:
        model = Post
        fields = ["title", "content", "tags"]  #2 author excluded (set automatically)

    def save(self, commit=True, user=None):
        post = super().save(commit=False)
        if user is not None:
            post.author = user   # assign logged-in user as author
        if commit:
            post.save()
        return post

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["content"]


