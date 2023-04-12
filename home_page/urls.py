from django.contrib.auth import views as auth_views
from django.urls import path, include
from . import views

urlpatterns = [
    # Home
    path("", views.home_view, name="index"),
]
