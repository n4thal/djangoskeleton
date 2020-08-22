from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Project


# Register your models here.
class ProjectAdmin(SummernoteModelAdmin):
    list_display = ('title', 'technology', 'publication_date')
    list_filter = ('technology', 'publication_date')
    search_fields = ('title', 'description')


admin.site.register(Project, ProjectAdmin)
