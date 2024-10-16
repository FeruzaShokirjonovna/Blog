from django.contrib import admin
from .models import Post, Comment
from django_summernote.admin import SummernoteModelAdmin


# Decorator for Posts
@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    # Set list of posts displayed by title, slug,status and created date
    list_display = ("title", "slug", "status", "created_on")
    search_fields = ["title", "content"]
    # Creates filter
    list_filter = ("status", "created_on")
    prepopulated_fields = {"slug": ("title",)}
    summernote_fields = "content"


# Decorator for Comments
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    # Set list of posts displayed by title, slug,status and created date
    list_display = ("name", "body", "post", "created_on", "approved")
    # Creates filter
    list_filter = ("approved", "created_on")
    search_fields = ("name", "email", "body")
    actions = ["approve_comments"]

    # Approve comments method
    # To approve the comment, set the field to true
    def approve_comments(self, request, queryset):
        queryset.update(approved=True)
