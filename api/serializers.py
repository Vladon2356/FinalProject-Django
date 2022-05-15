from rest_framework import serializers

from cinema_sessions.models import Sessions, Tickets
from halls.models import Halls
from movies.models import Movies, Genres, Actors, Producer
from users.models import CustomUser


class HallSerializer(serializers.ModelSerializer):
    class Meta:
        model = Halls
        fields = ["title", "rows", "columns"]


class GenresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genres
        fields = ["title"]


class ActorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actors
        fields = ["name"]


class ProducerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producer
        fields = ["name"]


class MovieDetailSerializer(serializers.ModelSerializer):
    genres = GenresSerializer(many=True)
    actors = ActorsSerializer(many=True)
    producer = ProducerSerializer(many=True)

    class Meta:
        model = Movies
        exclude = ["slug"]


class MovieListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movies
        fields = ["title", "year", "duration", "age_rating"]


class SessionListSerializer(serializers.ModelSerializer):
    movie = MovieDetailSerializer(read_only=True)
    hall = HallSerializer(read_only=True)

    class Meta:
        model = Sessions
        fields = ["movie", "hall", "date"]


class SessionDetailSerializer(serializers.ModelSerializer):
    movie = MovieDetailSerializer(read_only=True)
    hall = HallSerializer(read_only=True)

    class Meta:
        model = Sessions
        fields = ["movie", "hall", "date", "start_at", "end_at", "ticket_price"]


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        exclude = [
            "password",
            "is_staff",
            "user_permissions",
            "groups",
            "date_joined",
            "is_superuser",
            "last_login",
        ]


class UsersListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["id", "username", "age"]
