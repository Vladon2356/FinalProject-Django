from django.urls import path
from users import views

urlpatterns = [
    path("<int:pk>/", views.UserDetail.as_view(), name="profile"),
    # path('<str:slug>/', views.HallDetail.as_view(), name='hall_detail'),
]
