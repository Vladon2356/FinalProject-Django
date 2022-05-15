from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from halls.models import Halls


class HallsList(ListView):
    """Halls list page"""

    model = Halls
    template_name = "cinema/halls/hall_list.html"
    context_object_name = "halls"

    def get_queryset(self):
        return Halls.objects.all()
