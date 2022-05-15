from django.urls import path
from movies import views

urlpatterns = [
    path("", views.MoviesList.as_view(), name="movies_list"),
    path("<str:slug>/", views.MovieDetail.as_view(), name="movie_detail"),
]
