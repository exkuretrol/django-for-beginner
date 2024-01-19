from django.contrib import admin
from .models import Articles, Comment


class CommentAdmin(admin.ModelAdmin):
    date_hierarchy = "comment_datetime"
    list_display = ["article", "comment", "author"]
    # exclude= ["comment_datetime"]

class CommentInLine(admin.TabularInline):
# class CommentInLine(admin.StackedInline):
    model = Comment
    extra = 0


class ArticlesAdmin(admin.ModelAdmin):
    inlines = [CommentInLine]
    list_display = ["title", "body", "date", "author"]
    sortable_by = ["date"]


admin.site.register(Articles, ArticlesAdmin)
admin.site.register(Comment, CommentAdmin)
