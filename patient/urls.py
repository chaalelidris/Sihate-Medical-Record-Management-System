from django.urls import path, include
from .views import patient_profile

urlpatterns = [
    path("profile/", patient_profile, name="patient_profile"),
    path("appointment/", include("appointment.urls")),
]
