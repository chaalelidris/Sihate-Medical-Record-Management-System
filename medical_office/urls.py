from django.urls import path, include
from . import views


urlpatterns = [
    path("profile/", views.medicalOfficeProvileView, name="medical_office_profile"),
    path("appointment/", include("appointment.urls")),
]
