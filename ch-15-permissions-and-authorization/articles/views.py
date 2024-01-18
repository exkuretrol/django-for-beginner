from django.views.generic import ListView, CreateView, DetailView
from django.views.generic.edit import UpdateView, DeleteView
from .models import Articles
from django.urls import reverse_lazy


class ArticleListView(ListView):
    model = Articles
    context_object_name = "articles"
    template_name = "article_list.html"


class ArticleDetailView(DetailView):
    model = Articles
    context_object_name = "article"
    template_name = "article_detail.html"


class ArticleCreateView(CreateView):
    model = Articles
    fields = [
        "title",
        "body",
        "author",
    ]
    template_name = "article_create.html"


class ArticleUpdateView(UpdateView):
    model = Articles
    fields = ["title", "body"]
    template_name = "article_update.html"

    def get_success_url(self):
        return reverse_lazy("article_detail", kwargs={"pk": self.get_object().pk})


class ArticleDeleteView(DeleteView):
    model = Articles
    template_name = "article_delete.html"
    success_url = reverse_lazy("article_list")
