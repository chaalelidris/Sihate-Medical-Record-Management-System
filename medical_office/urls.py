from django.urls import path, include
from . import views


urlpatterns = [
    path("profile/", views.medical_office_profile, name="medical_office_profile"),
    path("appointment/", include("appointment.urls")),
]
