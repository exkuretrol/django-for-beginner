from django.views.generic import ListView, DetailView
from .models import Post

class BlogListView(ListView):
    context_object_name = "post_list"
    model = Post
    template_name = "home.html"

class PostDetailView(DetailView):
    context_object_name = "post"
    model = Post
    template_name = "post_detail.html"
