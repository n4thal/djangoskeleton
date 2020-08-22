from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Post, Comment


# Register your models here.
class PostAdmin(SummernoteModelAdmin):
    list_display = ('title', 'slug', 'status', 'publication_date')
    list_filter = ('status', 'publication_date')
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title', )}


@admin.register(Comment)
class CommentAdmin(SummernoteModelAdmin):
    list_display = ('name', 'body', 'post', 'publication_date', 'active')
    list_filter = ('active', 'publication_date')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)


admin.site.register(Post, PostAdmin)
