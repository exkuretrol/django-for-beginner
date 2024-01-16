from .views import BlogListView, PostDetailView, PostNewView, PostUpdateView, PostDeleteView
from django.urls import path

urlpatterns = [
    path("", BlogListView.as_view(), name="home"),
    path("post/<int:pk>/", PostDetailView.as_view(), name="post_detail"),
    path("post/new/", PostNewView.as_view(), name="post_new"),
    path("post/<int:pk>/edit/", PostUpdateView.as_view(), name="post_edit"),
    path("post/<int:pk>/delete/", PostDeleteView.as_view(), name="post_delete"),
]
