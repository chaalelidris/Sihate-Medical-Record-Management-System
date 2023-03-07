from django.urls import path, include
from .views import patient_profile, patientDashboardView

urlpatterns = [
    path("", patientDashboardView, name="patient_dashboard"),
    path("profile/", patient_profile, name="patient_profile"),
    path("appointment/", include("appointment.urls")),
]
