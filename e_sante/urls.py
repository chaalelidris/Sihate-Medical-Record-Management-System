from django.urls import path, include
from . import views

urlpatterns = [
    path("doctor/", include("doctor.urls")),
    path("patient/", include("patient.urls")),
    path("medical_office/", include("medical_office.urls")),
    path("logout/", views.logout, name="logout"),
    p,
]
