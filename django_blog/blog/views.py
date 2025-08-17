from django.shortcuts import render, redirect
from django import forms
from django.contrib import messages
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .forms import CustomUserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.urls import reverse_lazy, reverse
from django.urls import reverse_lazy, reverse
from .models import Post, Comment
from .forms import CommentForm
from django.db.models import Q
from django.shortcuts import render

def post_search(request):
    query = request.GET.get("q", "")
    results = []

    if query:
        results = Post.objects.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query) |
            Q(tags__name__icontains=query)
        ).distinct()  # distinct to avoid duplicates from many-to-many joins

    return render(request, "blog/post_search.html", {"query": query, "results": results})

def register_view(request):
    """Django's inbuilt authenticatioin view"""
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")
    else:
        form = CustomUserCreationForm()
    return render(request, "blog/register.html", {"form": form})

def home(request):
    return render(request, "blog/home.html")

def login_view(request):
    """Django's inbuilt login view"""
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirec("home")
    else:
        form = AuthenticationForm()
    return render(request, "blog/login.html", {"form": form})

def logout_view(request):
    logout(request)
    return redirect("home")

@login_required
def profile_view(request):
    """
    Profile management
    View and edit profile details eg email
    """
    if request.methos == "POST":
        form = ProfileForm(request.POST,instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated successfully.")
            return redirect("profile")
    else:
        form = ProfileForm(instance=request.user)

    return render(request, "blog/profile.html", {"form": form})

class PostListView(ListView):
    model = Post
    context_object_name = "posts"


class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ["title", "content"]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ["title", "content"]

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = reverse_lazy("post-list")

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

# List all comments for a specific post
class CommentListView(ListView):
    model = Comment
    template_name = "blog/comment_list.html"
    context_object_name = "comments"

    def get_queryset(self):
        post = get_object_or_404(Post, pk=self.kwargs["post_id"])
        return Comment.objects.filter(post=post).order_by("-created_at")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["post"] = get_object_or_404(Post, pk=self.kwargs["post_id"])
        return context


# Create new comment (directly on post)
class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentForm
    template_name = "blog/comment_form.html"

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.post = get_object_or_404(Post, pk=self.kwargs["post_id"])
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("post-detail", kwargs={"pk": self.kwargs["post_id"]})


# Update a comment (only author can edit)
class CommentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = "blog/comment_form.html"

    def test_func(self):
        comment = self.get_object()
        return self.request.user == comment.author

    def get_success_url(self):
        return reverse("post-detail", kwargs={"pk": self.object.post.pk})


# Delete a comment (only author can delete)
class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comment
    template_name = "blog/comment_confirm_delete.html"

    def test_func(self):
        comment = self.get_object()
        return self.request.user == comment.author

    def get_success_url(self):
        return reverse("post-detail", kwargs={"pk": self.object.post.pk})

def posts_by_tag(request, tag_name):
    tag = get_object_or_404(Tag, name=tag_name)
    posts = Post.objects.filter(tags=tag)
    return render(request, "blog/posts_by_tag.html", {"tag": tag, "posts": posts})
