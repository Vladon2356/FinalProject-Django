from django.contrib import admin
from halls.models import Halls


class HallAdmin(admin.ModelAdmin):
    list_display = ("title", "rows", "columns")
    list_display_links = ("title", "rows", "columns")
    search_fields = ("title", "rows", "columns")
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Halls, HallAdmin)
