from django.urls import path, include
from . import views

# Appointment urls
urlpatterns = {
    path("appointment", views.appointment_list, name="appointment_list"),
    path(
        "appointment/edit/<int:id>/)", views.edit_appointment, name="edit_appointment"
    ),
    path(
        "appointment/delete/<int:id>/)",
        views.delete_appointment,
        name="delete_appointment",
    ),
    path(
        "appointment/create_appointment",
        views.create_appointment,
        name="create_appointment",
    ),
    path(
        "appointment/annual_appointment/",
        views.annual_appointment,
        name="annual_appointment",
    ),
}
