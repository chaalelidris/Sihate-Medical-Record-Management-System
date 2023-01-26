from django.urls import path, include
from . import views

urlpatterns = [
    path("profile/", views.doctor_profile, name="doctor_profile"),
    path("patient_list", views.patient_list, name="patient_list"),
    path("prescription/", include("prescription.urls")),
    
    path("consultation_list/", views.consultation_list, name="consultation_list"),
    path(
        "consultation_list_patient/",
        views.consultation_list_patient,
        name="consultation_list_patient",
    ),
    path("consultation/", views.consultation, name="consultation"),
    path(
        "consultation_edit/<int:id_consultation>/",
        views.consultation_edit,
        name="consultation_edit",
    ),
    path(
        "consultation_delete/<int:id_consultation>/",
        views.consultation_delete,
        name="consultation_delete",
    ),
    path("statistique/", views.Data, name="Data"),
]
