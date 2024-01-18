from django.contrib import admin
from .models import Articles

class ArticlesAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "body",
        "date",
        "author"
    ]
    sortable_by = ["date"]
admin.site.register(Articles, ArticlesAdmin)
