from django.contrib import admin
from movies.models import Movies, Genres, Actors, Producer
from .models import *


class MoviesAdmin(admin.ModelAdmin):
    def formfield_for_manytomany(self, db_field, request, **kwargs):
        if db_field.name == "genres":
            kwargs["queryset"] = Genres.objects.all()
        if db_field.name == "actors":
            kwargs["queryset"] = Actors.objects.all()
        if db_field.name == "producer":
            kwargs["queryset"] = Producer.objects.all()
        return super().formfield_for_manytomany(db_field, request, **kwargs)

    list_display = ("title", "poster", "year", "age_rating", "in_rental")
    list_display_links = ("title",)
    search_fields = ("title", "year", "age_rating")
    list_filter = ("year", "age_rating", "genres", "actors", "producer")
    prepopulated_fields = {"slug": ("title",)}
    list_editable = ("in_rental", "age_rating")


class GenresAdmin(admin.ModelAdmin):
    list_display = ("title",)
    list_display_links = ("title",)
    search_fields = ("title",)
    prepopulated_fields = {"slug": ("title",)}


class ActorsAdmin(admin.ModelAdmin):
    list_display = ("name",)
    list_display_links = ("name",)
    search_fields = ("name",)
    prepopulated_fields = {"slug": ("name",)}


class ProducerAdmin(admin.ModelAdmin):
    list_display = ("name",)
    list_display_links = ("name",)
    search_fields = ("name",)
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(Movies, MoviesAdmin)
admin.site.register(Actors, ActorsAdmin)
admin.site.register(Producer, ProducerAdmin)
admin.site.register(Genres, GenresAdmin)
