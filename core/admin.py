from django.contrib import admin
from .models import Author, MetaInfo


# Register your models here.
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name', 'postcode', 'city', 'mail', 'phone')


class MetaInfoAdmin(admin.ModelAdmin):
    list_display = ('description', 'keywords')
    list_filter = ('description', 'keywords')
    search_fields = ('description', 'keywords')


admin.site.register(Author, AuthorAdmin)
admin.site.register(MetaInfo, MetaInfoAdmin)
