from django.urls import path, include
from .views import (
    appointment_list,
    create_appointment,
    edit_appointment,
    delete_appointment,
    yearly_appointment,
)

# Appointment urls
urlpatterns = [
    path("", appointment_list, name="appointment_list"),
    path("create_appointment/", create_appointment, name="create_appointment"),
    path("edit_appointment/<int:id>/", edit_appointment, name="edit_appointment"),
    path(
        "delete_appointment/<int:id>/",
        delete_appointment,
        name="delete_appointment",
    ),
    path("yearly_appointment/", yearly_appointment, name="yearly_appointment"),
]
