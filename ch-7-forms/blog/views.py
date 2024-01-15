from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Post


class BlogListView(ListView):
    context_object_name = "post_list"
    model = Post
    template_name = "home.html"


class PostDetailView(DetailView):
    context_object_name = "post"
    model = Post
    template_name = "post_detail.html"


class PostNewView(CreateView):
    model = Post
    template_name = "post_new.html"
    fields = ["title", "author", "body"]


class PostUpdateView(UpdateView):
    model = Post
    template_name = "post_edit.html"
    fields = ["title", "body"]


class PostDeleteView(DeleteView):
    model = Post
    template_name = "post_delete.html"
    success_url = reverse_lazy("home")
