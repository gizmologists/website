from django.contrib import admin
from .models import Person, Project

class ProjectAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Person)
admin.site.register(Project, ProjectAdmin)
