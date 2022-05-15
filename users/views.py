from django.urls import reverse_lazy
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

from users.models import CustomUser
from cinema_sessions.models import Tickets


class MainPageView(TemplateView):
    """Main page"""

    template_name = "base.html"


class UserDetail(LoginRequiredMixin, DetailView):
    """Profile page"""

    model = CustomUser
    template_name = "cinema/users/user_detail.html"
    context_object_name = "user"
    login_url = reverse_lazy("account_login")
    def get_queryset(self):

        return CustomUser.objects.filter(pk=self.kwargs["pk"])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tickets"] = Tickets.objects.filter(owner_id=self.kwargs["pk"])

        return context
