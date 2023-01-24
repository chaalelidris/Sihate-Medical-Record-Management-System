from django.urls import path, include
from . import views

urlpatterns = [
    path("profile/", views.patient_profile, name="patient_profile"),
    path("rd/", views.rd, name="rd"),
    path("create_meeting/", views.create_meeting, name="create_meeting"),
    path("rd_edit/<int:id>/", views.update_meeting, name="edit_meeting"),
    path("rd_delete/<int:id>/", views.delete_meeting, name="rd_delete"),
]
