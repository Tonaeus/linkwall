from django.urls import path

from . import views

app_name = "user"

urlpatterns = [
    path('<slug:slug>/', views.user_profile, name="user_profile"),
]