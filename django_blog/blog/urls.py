from django.urls import path
from . import views

urlpatterns = [
        path("", views.home, name="home"),
        path("login/", views.login_view, name="login"),
        path("logout/", views.logout_view, name="logout"),
        path("register/", views.register_view, name="register"),
        path("profile/", views.profile_view, name="profile"),
        path("post/", views.PostListView.as_view(), name="post-list"),
        path("post/new/", views.PostCreateView.as_view(), name="post-create"),
        path("post/<int:pk>/", views.PostDetailView.as_view(), name="post-detail"),
        path("post/<int:pk>/update/", views.PostUpdateView.as_view(), name="post-update"),
        path("post/<int:pk>/delete/", views.PostDeleteView.as_view(), name="post-delete"),
        path("comments/<int:pk>/edit/", views.CommentUpdateView.as_view(), name="comment-update"),
        path("comments/<int:pk>/delete/", views.CommentDeleteView.as_view(), name="comment-delete"),
        ]

