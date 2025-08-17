from django.urls import path
from . import views

urlpatterns = [
        path("", views.home, name="home"),
        path("login/", views.login_view, name="login"),
        path("logout/", views.logout_view, name="logout"),
        path("register/", views.register_view, name="register"),
        path("profile/", views.profile_view, name="profile"),
        path("posts/<int:post_id>/comments/new/", views.CommentCreateView.as_view(), name="comment-create"),
        path("comments/<int:pk>/edit/", views.CommentUpdateView.as_view(), name="comment-update"),
        `path("comments/<int:pk>/delete/", views.CommentDeleteView.as_view(), name="comment-delete"),
        ]

