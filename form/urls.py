from django.urls import path

from . import views

app_name = "form"

urlpatterns = [
    path("edit-profile", views.edit_profile, name="edit_profile"),
]