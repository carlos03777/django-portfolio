
# Register your models here.
from django.contrib import admin
from .models import Project, Technology




@admin.register(Technology)
class TechnologyAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ("name",)

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "is_published", "order", "created_at")
    list_filter = ("is_published", "technologies")
    search_fields = ("title", "excerpt", "description")
    prepopulated_fields = {"slug": ("title",)}
    filter_horizontal = ("technologies",)
