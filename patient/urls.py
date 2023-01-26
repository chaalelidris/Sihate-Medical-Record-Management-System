from django.urls import path, include
from . import views

urlpatterns = [
    path("profile/", views.patient_profile, name="patient_profile"),
    path("appointment/", include("appointment.urls")),
]
