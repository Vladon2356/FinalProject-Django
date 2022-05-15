from django.urls import path
from halls import views

urlpatterns = [
    path("", views.HallsList.as_view(), name="halls_list"),
]
