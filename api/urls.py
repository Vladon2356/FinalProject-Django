from django.urls import path
from api import views

urlpatterns = [
    path("movies/", views.MoviesListView.as_view()),
    path("movies/<int:pk>/", views.MoviesDetailView.as_view()),
    path("sessions/", views.SessionListView.as_view()),
    path("sessions/<int:pk>/", views.SessionDetailView.as_view()),
    path("halls/", views.HallsListView.as_view()),
    path("halls/<int:pk>/", views.HallDetailView.as_view()),
    path("users/", views.UsersListView.as_view()),
    path("users/<int:pk>/", views.UserDetailView.as_view()),
]
