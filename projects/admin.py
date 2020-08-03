from django.contrib import admin
from .models import Project


# Register your models here.
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'technology', 'publication_date')
    list_filter = ('technology', 'publication_date')
    search_fields = ('title', 'description')


admin.site.register(Project, ProjectAdmin)
