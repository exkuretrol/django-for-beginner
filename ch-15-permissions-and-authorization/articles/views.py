from django.views.generic import ListView, CreateView, DetailView
from django.views.generic.edit import UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from .models import Articles
from django.urls import reverse_lazy


class ArticleListView(LoginRequiredMixin, ListView):
    model = Articles
    context_object_name = "articles"
    template_name = "article_list.html"


class ArticleDetailView(LoginRequiredMixin, DetailView):
    model = Articles
    context_object_name = "article"
    template_name = "article_detail.html"


class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Articles
    fields = [
        "title",
        "body",
    ]
    template_name = "article_create.html"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class ArticleUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Articles
    fields = ["title", "body"]
    template_name = "article_update.html"

    def get_success_url(self):
        return reverse_lazy("article_detail", kwargs={"pk": self.get_object().pk})
    
    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


class ArticleDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Articles
    template_name = "article_delete.html"
    success_url = reverse_lazy("article_list")

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user
