import datetime

from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin


from cinema_sessions.models import Sessions, Tickets


class SessionList(ListView):
    """Sessions list page"""

    model = Sessions
    template_name = "cinema/sessions/session_list.html"
    context_object_name = "sessions"

    def get_queryset(self):
        return Sessions.objects.filter(is_active=True)


class SessionDetail(DetailView):
    """Session detail page"""

    model = Sessions
    template_name = "cinema/sessions/session_detail.html"
    context_object_name = "session"


    def get_queryset(self):
        return Sessions.objects.filter(pk=self.kwargs["pk"], is_active=True)


class SessionsByMovie(ListView):
    """List session by moview page"""

    model = Sessions
    template_name = "cinema/sessions/session_list.html"
    context_object_name = "sessions"

    def get_queryset(self):
        return Sessions.objects.filter(
            movie__slug=self.kwargs["movie_slug"], is_active=True
        )


class SessionSearch(ListView):
    """Search sessions page"""

    model = Sessions
    template_name = "cinema/sessions/session_search.html"
    context_object_name = "sessions"

    def post(self, request, *args, **kwargs):
        filters = {}
        movie_id = int(request.POST.get("movie_id", 0))
        date_str = request.POST.get("date", "")
        if date_str:
            month, day, year = [int(i) for i in date_str.split("/")]
            date = datetime.date(day=day, month=month, year=year)
        else:
            date = datetime.date(day=1, month=1, year=2000)
        genres = request.POST.get("genres", "")
        actors = request.POST.get("actors", "")
        producer = request.POST.get("producers", "")
        if movie_id != 0:
            filters["movie_id"] = movie_id
        if date != datetime.date(2000, 1, 1):
            filters["date"] = date
        if genres:
            filters["movie__genres__title__contains"] = genres
        if actors:
            filters["movie__actors__name__contains"] = actors
        if producer:
            filters["movie__producer__name__contains"] = producer
        sessions = Sessions.objects.filter(**filters)
        return render(
            request,
            template_name="cinema/sessions/session_list.html",
            context={"sessions": sessions},
        )


class BuyTicket(LoginRequiredMixin, DetailView):
    """Buy ticket page"""

    movies = Sessions
    template_name = "cinema/tickets/ticket_reserve.html"
    context_object_name = "session"
    login_url = reverse_lazy("account_login")

    def post(self, request, *args, **kwargs):
        row, column = [int(i) for i in request.POST.get("res").split("-")]

        session_id = self.kwargs["pk"]

        owner_id = request.user.id
        message = Tickets.buy_ticket(
            session_id=session_id, row=row, column=column, owner_id=owner_id
        )
        return render(
            request,
            template_name="cinema/tickets/ticket_message.html",
            context={"message": message},
        )

    def get_queryset(self):
        return Sessions.objects.filter(pk=self.kwargs["pk"])
