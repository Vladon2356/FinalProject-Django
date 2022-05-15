from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from movies.models import Movies


class MoviesList(ListView):
    """Movies list page"""

    model = Movies
    template_name = "cinema/movies/movie_list.html"
    context_object_name = "movies"

    def get_queryset(self):
        return Movies.objects.filter(in_rental=True)


class MovieDetail(DetailView):
    """Movie detail page"""

    model = Movies
    template_name = "cinema/movies/movie_detail.html"
    context_object_name = "movie"

    def get_queryset(self):
        return Movies.objects.filter(slug=self.kwargs["slug"])
