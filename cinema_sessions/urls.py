from django.urls import path
from cinema_sessions import views

urlpatterns = [
    path("", views.SessionList.as_view(), name="sessions_list"),
    path("<int:pk>/", views.SessionDetail.as_view(), name="session_detail"),
    path("search/", views.SessionSearch.as_view(), name="session_search"),
    path("<str:movie_slug>/", views.SessionsByMovie.as_view(), name="session_by_movie"),
    path("<int:pk>/buy/ticket/", views.BuyTicket.as_view(), name="session_buy_ticket"),
]
