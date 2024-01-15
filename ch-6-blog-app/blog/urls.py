from .views import BlogListView, PostDetailView
from django.urls import path

urlpatterns = [
    path("", BlogListView.as_view(), name="home"),
    path("post/<int:pk>/", PostDetailView.as_view(), name="post_detail"),
]
