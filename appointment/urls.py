from django.urls import path, include
from . import views

# Appointment urls
urlpatterns = {
    path(
        "create_appointment/",
        views.create_appointment,
        name="create_appointment",
    ),
    path("", views.appointment_list, name="appointment_list"),
    path("edit/<int:id>/)", views.edit_appointment, name="edit_appointment"),
    path(
        "delete/<int:id>/)",
        views.delete_appointment,
        name="delete_appointment",
    ),
    path(
        "yearly_appointment/",
        views.yearly_appointment,
        name="yearly_appointment",
    ),
}
