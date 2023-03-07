from django.urls import path, include
from . import views

# doctor/urls
urlpatterns = [
    path("", views.doctorDashboardView, name="doctor_dashboard"),
    path("profile/", views.profileView, name="doctor_profile"),
    path("patient_list", views.patientListView, name="patient_list"),
    path("patient_list/medical_file/", include("medicalfile.urls")),
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
        views.updateConsultationView,
        name="consultation_edit",
    ),
    path(
        "consultation_delete/<int:id_consultation>/",
        views.deleteConsultationView,
        name="consultation_delete",
    ),
    path("statistique/", views.Data, name="Data"),
]
