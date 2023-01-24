from django.urls import path, include
from . import views


urlpatterns = [
    path("profile/", views.medical_office_profile, name="medical_office_profile"),
    path("annual_meeting", views.annual_meeting, name="annual_meeting"),
]
