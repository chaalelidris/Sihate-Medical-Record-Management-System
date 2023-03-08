from django.urls import path
from . import views

urlpatterns = [
    path("", views.homeView.as_view(), name="index"),
    path("login/", views.user_login, name="login"),
    # path("contact", views.contact, name="contact"),
]
