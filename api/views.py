from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView

from api import serializers
from cinema_sessions.models import Sessions
from halls.models import Halls
from movies.models import Movies
from users.models import CustomUser


class MoviesDetailView(RetrieveAPIView):
    """Movie detail"""

    queryset = Movies.objects.filter(in_rental=True)
    serializer_class = serializers.MovieDetailSerializer


class MoviesListView(ListAPIView):
    """Movie list"""

    queryset = Movies.objects.filter(in_rental=True)
    serializer_class = serializers.MovieListSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filter_fields = ["actors", "genres", "producer", "year", "age_rating"]
    search_fields = ["actors", "genres", "producer", "year", "title"]


class SessionDetailView(RetrieveAPIView):
    """Session detail"""

    queryset = Sessions.objects.filter(is_active=True)
    serializer_class = serializers.SessionDetailSerializer


class SessionListView(ListAPIView):
    """Sessions list"""

    queryset = Sessions.objects.filter(is_active=True)
    serializer_class = serializers.SessionListSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filter_fields = ["movie", "ticket_price", "date", "hall"]
    search_fields = ["movie", "ticket_price", "date", "hall"]


class HallDetailView(RetrieveAPIView):
    """Hall detail"""

    queryset = Halls.objects.all()
    serializer_class = serializers.HallSerializer


class HallsListView(ListAPIView):
    """Halls list"""

    queryset = Halls.objects.all()
    serializer_class = serializers.HallSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filter_fields = ["title"]
    search_fields = ["title"]


class UserDetailView(RetrieveAPIView):
    """User detail"""

    queryset = CustomUser.objects.filter(is_active=True)
    serializer_class = serializers.UserDetailSerializer


class UsersListView(ListAPIView):
    """Users list"""

    queryset = CustomUser.objects.filter(is_active=True)
    serializer_class = serializers.UsersListSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filter_fields = ["username", "age"]
    search_fields = ["username", "age"]
