from django import template
from movies.models import Genres, Actors, Producer, Movies
from cinema_sessions.models import Tickets

register = template.Library()


@register.filter(name="range")
def generate_range(n: int):
    return range(1, n + 1)


@register.simple_tag(name="check_ticket")
def check_ticket(session_id: int, row: int, column: int):
    ticket = Tickets.objects.get(session_id=session_id, row=row, column=column)
    return ticket.sold


@register.simple_tag
def get_movies():
    return Movies.objects.filter(in_rental=True)


@register.simple_tag
def get_genres():
    return Genres.objects.all()


@register.simple_tag
def get_actors():
    return Actors.objects.all()


@register.simple_tag
def get_producers():
    return Producer.objects.all()
